from itertools import dropwhile, takewhile
import requests

def download_tarzan():
    return requests.get("http://www.gutenberg.org/cache/epub/78/pg78.txt").text

def stream_chapters(lines):
    """
    yield chapter_no, chapter_title, chapter_text

    where chapter_no is the chapter number (from the text)
    chapter_title is the title for the chapter (from the text)
    chapter_text is "\n\n" delimited lines of text.
    """
    def is_not_chapter(line):
        return not line.startswith('Chapter')
    def is_not_ending(line):
        return is_not_chapter(line) and not line.startswith('***')
    it = dropwhile(is_not_chapter, lines)
    chapter_no = next(it)
    next_no = None
    while (it):
        _ = next(it)
        chapter_title = next(it)
        chapter_lines = []
        for line in it:
            if is_not_ending(line):
                line = line.strip()
                if line:
                    chapter_lines.append(line)
            elif is_not_chapter(line):
                # at the end of the book
                it = None
                break
            else:
                # at the end of the chapter
                next_no = line
                break
        yield (chapter_no, chapter_title, '\n\n'.join(chapter_lines))
        chapter_no = next_no
