# A Curious Shebang
If you've ever written a shell script, you might top your script with your interpreter of choice (i.e. `#!/bin/python` or `#!/bin/bash`). What you might not have known that `rm` is also a valid interpreter. Take the following script.

```bash
#!/bin/rm
echo "Hello, world"
```

It would simply interpret to be removed. Useful? No. Hilarious? Yes.