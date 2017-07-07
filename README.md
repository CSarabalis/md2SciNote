# md2notes

**md2notes** is a rude little python program that converts notes with latex taken in markdown into html using [strapdown.js](http://strapdownjs.com/) and [MathJax](https://www.mathjax.org/).  

**Syntax:**
* Math is delimited by `\(` and `\)` (inline) and `\[` and `\]` and is rendered with MathJax.
* Output from the linux `date` command is formatted by the parser by including a line with `#(your_date_here)`.

**Terminal Commands:**
* `mdgen LOG` produces an html file LOG.html.
	* `-r` option refreshes all visible tabs of Chrome after compiling .html file.
	* `-o` option opens a new tab in Chrome to display .html file.
* `mddir name_to_search your_directory` searches for markdown files in the specified directory and runs `mdgen` on them
  * Example: `mddir LOG` finds all files called LOG in the current directory (plus subdirectories) and generates an html file LOG.html
* `indexgen filename_to_index index_filename` produces a html file INDEX.html which has a directory structure and has links to all LOG files.

**Sublime Compiler:**
* [Instructions](./sublime_compiler) to compile and view .html directly from Sublime

## Known issues

* **`mdgen` on OSX:** The `-r` and `-o` options use the linux bash command `google-chrome` to inteface with chrome. There isn't an equivalent command on OSX, so I recommend adding a file called `google-chrome` to a local `/bin` on your path:
```
#!/bin/bash

# Call chrome from command line
    site=""
    if [[ -f "$(pwd)/$1" ]]; then
        site="file://$(pwd)/$1"
    elif [[ "$1" == '/'* ]]; then
        site="file://$1"
    elif [[ "$1" =~ "^http" ]]; then
        site="$1"
    else
        site="http://$1"
    fi

    /usr/bin/open -a "/Applications/Google Chrome.app" "$site"
```
