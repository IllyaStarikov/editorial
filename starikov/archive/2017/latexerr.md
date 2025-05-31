# latexerr
The most frustrating thing about compiling LaTeX in a terminal is the wall of text that gets written to stdout. An easy solution would be piping to `dev/null`; except then you wouldn’t be able to get error messages (even if only pipe stdout to `dev/null` and keep stderr). So, I made a solution that handles the compiling by piping error messages to `less`. The syntax of `latexerr FILENAME` will compile the files. Passing `--clean` will delete temporary LaTeX files.

```
#!/bin/bash

# USAGE: ./script FILE --clean --glossary

extensions_to_delete=(\
	gz fls fdb_latexmk blg bbl log\
    aux out nav toc snm glg glo xdy
)

compile_and_open() {
    argument="$1"
    auxname="${argument%.tex}.aux"
    errors=$(pdflatex -shell-escape -interaction=nonstopmode -file-line-error "$argument" | grep ".*:[0-9]*:.*")

    if [[ -n $errors ]]; then
        echo "$1 Errors Detected"
        echo "$errors" | less
    else
        open_file $1
        echo "$1 Compile Successful"
    fi
}

open_file() {
    filename=`echo "$1" | cut -d'.' -f1`
    open "$filename.pdf"
    echo "$filename Opened"
}

# http://tex.stackexchange.com/questions/6845/compile-latex-with-bibtex-and-glossaries
glossary() {
    compile $1
    makeglossaries $1
    compile $1
    compile $1
}

clean() {
    for file in $(dirname $1)/*; do
        filename=$(basename "$file")
        extension="${filename##*.}"
        filename="${filename%.*}"

        for bad_extensions in "${extensions_to_delete[@]}" ; do
            if [[ $bad_extensions = $extension ]]; then
                rm $file
                echo "$file Deleted"
            fi
        done
    done
}

main() {
    compile_and_open $1

    if [ "$3" = "--glossary" ]; then
       glossary $1
    fi

    if [ "$2" = "--clean" ]; then
        clean $1
    fi

}

main "$@"
```

Updated version(s) will be posted [here](https://gist.github.com/IllyaStarikov/d20bdf0c4efd9022610f582a21818596).
