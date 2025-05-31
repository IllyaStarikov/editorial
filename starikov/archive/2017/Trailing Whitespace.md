# Trailing Whitespace
One of the most frustrating things to deal with is the trailing space. Trailing spaces are such a pain because

- They can screw up string literals
- They can break expectations in a text editor (i.e. jumping to a new line or the end of the line)
- They can actually break programming languages
- They are just unflattering

However, in Vim, it takes one `autocmd` to alleviate this.

```vim
augroup spaces
autocmd!
autocmd BufWritePre \* %s/s+$//e
augroup END
```

On every buffer save substitute spaces at the end of the line with nothing. Easy!