#!/usr/bin/env python3
"""
iPaste Sync Tool - Syncs local markdown files to remote server
"""

import os
import sys
import json
import hashlib
import argparse
import subprocess
import tempfile
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import logging


class IPasteSync:
    def __init__(self, config: Dict):
        self.local_path = Path(config['local_path']).expanduser()
        self.remote_host = config['remote_host']
        self.remote_path = config['remote_path']
        self.ssh_user = config.get('ssh_user')
        self.ssh_port = config.get('ssh_port', 22)
        self.ssh_key = config.get('ssh_key')
        self.dry_run = config.get('dry_run', False)
        self.verbose = config.get('verbose', False)

        # Setup logging
        log_level = logging.DEBUG if self.verbose else logging.INFO
        logging.basicConfig(
            level=log_level,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

        # Build SSH command prefix
        self.ssh_cmd = ['ssh']
        if self.ssh_user:
            self.ssh_cmd.extend([f'{self.ssh_user}@{self.remote_host}'])
        else:
            self.ssh_cmd.append(self.remote_host)

        if self.ssh_port != 22:
            self.ssh_cmd.extend(['-p', str(self.ssh_port)])

        if self.ssh_key:
            self.ssh_cmd.extend(['-i', os.path.expanduser(self.ssh_key)])

        # Add common SSH options
        self.ssh_cmd.extend(['-o', 'BatchMode=yes', '-o', 'ConnectTimeout=10'])

    def calculate_file_hash(self, filepath: Path) -> str:
        """Calculate SHA256 hash of a file."""
        sha256_hash = hashlib.sha256()
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def get_local_files(self) -> Dict[str, Dict]:
        """Get all markdown files from local directory with their metadata."""
        files = {}
        for filepath in self.local_path.rglob('*.md'):
            if filepath.is_file():
                relative_path = filepath.relative_to(self.local_path)
                files[str(relative_path)] = {
                    'path': filepath,
                    'hash': self.calculate_file_hash(filepath),
                    'mtime': filepath.stat().st_mtime,
                    'size': filepath.stat().st_size
                }
        return files

    def get_remote_files(self) -> Dict[str, Dict]:
        """Get all markdown files from remote directory with their metadata."""
        # Create a script to run on the remote server
        remote_script = f'''
import os
import hashlib
import json

def get_file_hash(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

remote_path = "{self.remote_path}"
files = {{}}

for root, dirs, filenames in os.walk(remote_path):
    for filename in filenames:
        if filename.endswith('.md'):
            filepath = os.path.join(root, filename)
            relative_path = os.path.relpath(filepath, remote_path)
            try:
                stat = os.stat(filepath)
                files[relative_path] = {{
                    'hash': get_file_hash(filepath),
                    'mtime': stat.st_mtime,
                    'size': stat.st_size
                }}
            except Exception as e:
                pass

print(json.dumps(files))
'''

        try:
            # Use stdin to pass the script to avoid shell escaping issues
            cmd = self.ssh_cmd + ['python3']
            result = subprocess.run(cmd, input=remote_script, capture_output=True, text=True, check=True)
            return json.loads(result.stdout)
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to get remote files: {e.stderr}")
            return {}
        except json.JSONDecodeError:
            self.logger.error("Failed to parse remote file list")
            return {}

    def ensure_remote_directory(self, remote_dir: str):
        """Ensure remote directory exists."""
        cmd = self.ssh_cmd + [f'mkdir -p "{remote_dir}"']
        try:
            subprocess.run(cmd, check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to create directory {remote_dir}: {e.stderr}")
            raise

    def copy_file(self, local_file: Path, remote_relative_path: str):
        """Copy a single file to the remote server."""
        remote_full_path = os.path.join(self.remote_path, remote_relative_path)
        remote_dir = os.path.dirname(remote_full_path)

        # Ensure remote directory exists
        self.ensure_remote_directory(remote_dir)

        # Build SCP command
        scp_cmd = ['scp', '-P', str(self.ssh_port)]
        if self.ssh_key:
            scp_cmd.extend(['-i', os.path.expanduser(self.ssh_key)])

        # Add source and destination
        if self.ssh_user:
            dest = f"{self.ssh_user}@{self.remote_host}:{remote_full_path}"
        else:
            dest = f"{self.remote_host}:{remote_full_path}"

        scp_cmd.extend([str(local_file), dest])

        try:
            subprocess.run(scp_cmd, check=True, capture_output=True)
            # Set permissions to be readable
            chmod_cmd = self.ssh_cmd + [f'chmod 644 "{remote_full_path}"']
            subprocess.run(chmod_cmd, check=True, capture_output=True)
            return True
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to copy {local_file}: {e.stderr}")
            return False

    def delete_remote_file(self, remote_relative_path: str):
        """Delete a file from the remote server."""
        remote_full_path = os.path.join(self.remote_path, remote_relative_path)
        cmd = self.ssh_cmd + [f'rm -f "{remote_full_path}"']

        try:
            subprocess.run(cmd, check=True, capture_output=True)
            return True
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to delete {remote_relative_path}: {e.stderr}")
            return False

    def sync(self):
        """Perform the sync operation."""
        self.logger.info("Starting iPaste sync...")

        # Get file lists
        self.logger.info("Scanning local files...")
        local_files = self.get_local_files()
        self.logger.info(f"Found {len(local_files)} local markdown files")

        self.logger.info("Scanning remote files...")
        remote_files = self.get_remote_files()
        self.logger.info(f"Found {len(remote_files)} remote markdown files")

        # Determine operations needed
        to_add = []
        to_update = []
        to_delete = []

        # Check for files to add or update
        for rel_path, local_info in local_files.items():
            if rel_path not in remote_files:
                to_add.append(rel_path)
            elif local_info['hash'] != remote_files[rel_path]['hash']:
                to_update.append(rel_path)

        # Check for files to delete (exist on remote but not local)
        for rel_path in remote_files:
            if rel_path not in local_files:
                to_delete.append(rel_path)

        # Report what will be done
        total_ops = len(to_add) + len(to_update) + len(to_delete)
        if total_ops == 0:
            self.logger.info("Everything is up to date!")
            return

        self.logger.info(f"\nSync plan:")
        if to_add:
            self.logger.info(f"  Add: {len(to_add)} files")
            if self.verbose:
                for f in to_add[:5]:
                    self.logger.debug(f"    + {f}")
                if len(to_add) > 5:
                    self.logger.debug(f"    ... and {len(to_add) - 5} more")

        if to_update:
            self.logger.info(f"  Update: {len(to_update)} files")
            if self.verbose:
                for f in to_update[:5]:
                    self.logger.debug(f"    ~ {f}")
                if len(to_update) > 5:
                    self.logger.debug(f"    ... and {len(to_update) - 5} more")

        if to_delete:
            self.logger.info(f"  Delete: {len(to_delete)} files")
            if self.verbose:
                for f in to_delete[:5]:
                    self.logger.debug(f"    - {f}")
                if len(to_delete) > 5:
                    self.logger.debug(f"    ... and {len(to_delete) - 5} more")

        if self.dry_run:
            self.logger.info("\nDry run mode - no changes will be made")
            return

        # Execute operations
        success_count = 0
        error_count = 0

        # Process additions and updates
        for rel_path in to_add + to_update:
            action = "Adding" if rel_path in to_add else "Updating"
            self.logger.info(f"{action} {rel_path}")
            if self.copy_file(local_files[rel_path]['path'], rel_path):
                success_count += 1
            else:
                error_count += 1

        # Process deletions
        for rel_path in to_delete:
            self.logger.info(f"Deleting {rel_path}")
            if self.delete_remote_file(rel_path):
                success_count += 1
            else:
                error_count += 1

        # Summary
        self.logger.info(f"\nSync complete: {success_count} succeeded, {error_count} failed")

        if error_count > 0:
            self.logger.warning("Some operations failed - check logs above")
            sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description='Sync markdown files to iPaste server')
    parser.add_argument('-c', '--config', default='configuration.json',
                        help='Configuration file path (default: configuration.json)')
    parser.add_argument('-l', '--local-path', help='Override local path')
    parser.add_argument('-r', '--remote-host', help='Override remote host')
    parser.add_argument('-p', '--remote-path', help='Override remote path')
    parser.add_argument('-u', '--ssh-user', help='Override SSH user')
    parser.add_argument('--ssh-port', type=int, help='Override SSH port')
    parser.add_argument('-k', '--ssh-key', help='Override SSH key path')
    parser.add_argument('-n', '--dry-run', action='store_true',
                        help='Show what would be done without making changes')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Enable verbose logging')

    args = parser.parse_args()

    # Load configuration
    try:
        with open(args.config, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print(f"Error: Configuration file '{args.config}' not found")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in configuration file '{args.config}'")
        sys.exit(1)

    # Override config with command line arguments
    if args.local_path:
        config['local_path'] = args.local_path
    if args.remote_host:
        config['remote_host'] = args.remote_host
    if args.remote_path:
        config['remote_path'] = args.remote_path
    if args.ssh_user:
        config['ssh_user'] = args.ssh_user
    if args.ssh_port:
        config['ssh_port'] = args.ssh_port
    if args.ssh_key:
        config['ssh_key'] = args.ssh_key
    if args.dry_run:
        config['dry_run'] = True
    if args.verbose:
        config['verbose'] = True

    # Validate required fields
    required_fields = ['local_path', 'remote_host', 'remote_path']
    for field in required_fields:
        if field not in config:
            print(f"Error: Missing required field '{field}' in configuration")
            sys.exit(1)

    # Run sync
    try:
        syncer = IPasteSync(config)
        syncer.sync()
    except KeyboardInterrupt:
        print("\nSync interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
