# Vim Autorun
One of the reasons I kept [CodeRunner](https://coderunnerapp.com) handy was its ability to quickly compile code. With a single click of a button, I could run any of my frequently used languages. It didn’t matter if it was an interpreted or compiled language, so I could virtually run anything, like:  

- C/C
- Python
- Lua
- LaTeX
- Perl

However, in the last few months I started using Vim. *Heavily*. So much so I was trying to use Vim command in the CodeRunner buffers. So I decided I wanted to have the functionality, and in vim-esque fashion, I mapped to my leader key: `<leader>r`. The mnemonic `<leader>r`un helped me remember the command on the first few tries.

To get the functionality, just add the following to your `.vimrc`.

```vim
function! MakeIfAvailable()
    if filereadable("./makefile")
        make
    elseif (&filetype == "cpp")
        execute("!clang++ -std=c++14" + bufname("%"))
        execute("!./a.out")
    elseif (&filetype == "c")
        execute("!clang -std=c11" + bufname("%"))
        execute("!./a.out")
    elseif (&filetype == "tex")
        execute("!xelatex" + bufname("%"))
        execute("!open" + expand(%:r))
    endif
endfunction

augroup spaces
    autocmd!
    autocmd FileType c nnoremap <leader>r :call MakeIfAvailable()<cr>
    autocmd FileType cpp nnoremap <leader>r :call MakeIfAvailable()<cr>
    autocmd FileType tex nnoremap <leader>r :call MakeIfAvailable()<cr>
    autocmd FileType python nnoremap <leader>r :exec '!python' shellescape(@%, 1)<cr>
    autocmd FileType perl nnoremap <leader>r :exec '!perl' shellescape(@%, 1)<cr>
    autocmd FileType sh nnoremap <leader>r :exec '!bash' shellescape(@%, 1)<cr>
    autocmd FileType swift nnoremap <leader>r :exec '!swift' shellescape(@%, 1)<cr>
    nnoremap <leader>R :!<Up><CR>
augroup END
```