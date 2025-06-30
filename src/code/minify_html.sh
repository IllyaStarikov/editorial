#!/bin/bash

# HTML Minification Script
# Minifies all *.html files in the project and saves them as *.min.html
# Uses html-minifier-terser for advanced minification

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if html-minifier-terser is installed
if ! command -v html-minifier-terser &> /dev/null; then
    print_error "html-minifier-terser is not installed."
    print_status "Installing html-minifier-terser globally..."
    npm install -g html-minifier-terser
    if [ $? -ne 0 ]; then
        print_error "Failed to install html-minifier-terser. Please install it manually:"
        print_error "npm install -g html-minifier-terser"
        exit 1
    fi
fi

# Get the project root (src directory)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

print_status "Starting HTML minification process..."
print_status "Project root: $PROJECT_ROOT"

# Counter for processed files
PROCESSED=0
SKIPPED=0
ERRORS=0

# Find all HTML files and process them
while IFS= read -r -d '' file; do
    # Get the directory and filename
    dir=$(dirname "$file")
    filename=$(basename "$file")
    name_without_ext="${filename%.*}"
    
    # Skip if it's already a minified file
    if [[ "$filename" == *.min.html ]]; then
        print_warning "Skipping already minified file: $file"
        ((SKIPPED++))
        continue
    fi
    
    # Create output filename
    output_file="$dir/${name_without_ext}.min.html"
    
    print_status "Minifying: $file -> $output_file"
    
    # Minify the HTML file
    if html-minifier-terser \
        --collapse-whitespace \
        --remove-comments \
        --remove-optional-tags \
        --remove-redundant-attributes \
        --remove-script-type-attributes \
        --remove-tag-whitespace \
        --use-short-doctype \
        --minify-css \
        --minify-js \
        --minify-urls \
        --sort-attributes \
        --sort-class-name \
        --decode-entities \
        --remove-empty-attributes \
        --remove-empty-elements \
        --output "$output_file" \
        "$file"; then
        
        # Get file sizes for comparison
        original_size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null || echo "unknown")
        minified_size=$(stat -f%z "$output_file" 2>/dev/null || stat -c%s "$output_file" 2>/dev/null || echo "unknown")
        
        if [[ "$original_size" != "unknown" && "$minified_size" != "unknown" ]]; then
            reduction=$((original_size - minified_size))
            percentage=$(( (reduction * 100) / original_size ))
            print_status "  ✓ Reduced by ${reduction} bytes (${percentage}%): ${original_size} -> ${minified_size}"
        else
            print_status "  ✓ Minification completed"
        fi
        
        ((PROCESSED++))
    else
        print_error "Failed to minify: $file"
        ((ERRORS++))
    fi
    
done < <(find "$PROJECT_ROOT" -name "*.html" -type f -print0)

# Print summary
echo
print_status "=== Minification Summary ==="
print_status "Files processed: $PROCESSED"
if [ $SKIPPED -gt 0 ]; then
    print_warning "Files skipped: $SKIPPED"
fi
if [ $ERRORS -gt 0 ]; then
    print_error "Files with errors: $ERRORS"
    exit 1
else
    print_status "All files processed successfully!"
fi
