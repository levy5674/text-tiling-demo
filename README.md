# text-tiling-demo

This is a demonstration of nltk's implementation of TextTiling.   http://www.nltk.org/_modules/nltk/tokenize/texttiling.html

TextTiling is from the paper

```
M. A. Hearst. Texttiling: Segmenting text into
multi-paragraph subtopic passages. Computational
linguistics, 23(1):33–64, 1997
```

in this demo I download tarzan from project gutenberg - http://www.gutenberg.org/cache/epub/78/pg78.txt

and process it like this:

- split it into chapters
- munge chapter one so each line is its own paragraph
- run text tiling on those
- reformat the tiles as paragraphs and print them out

## Installation / Demo

Assumes miniconda (python 2.7) has already been installed.  If not, it comes from here https://conda.io/miniconda.html

```
# setup the python environment
conda env create
source activate text-tiling-demo

# install nltk stopwords
python -m nltk.downloader stopwords

# run the Demo
python -m text_tiling_demo.demo
```

## Future directions
- get tarzan from nltk corpus instead of downloading it
- tune parameters
