# md2notes

**md2notes** is a rude little python program that converts notes with latex taken in markdown into html using [strapdown.js](http://strapdownjs.com/).  

**Syntax:**
* Math is delimited by \( and \) (inline) and \[ and \] and is rendered with MathJax.
* Output from the linux `date` command is formatted by the parser.

**Terminal Commands:**
* `mdgen LOG` produces an html file LOG.html.
* `mddir name_to_search your_directory` searches for markdown files in the specified directory and runs `mdgen` on them
  * Example: `mddir LOG` finds all files called LOG in the current directory (plus subdirectories) and generates an html file LOG.html
