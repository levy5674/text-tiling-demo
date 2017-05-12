if __name__ == '__main__':
    from nltk.tokenize import TextTilingTokenizer
    import get_data
    ttt = TextTilingTokenizer()
    chapter_iter = get_data.stream_chapters(
            get_data.download_tarzan().split('\r\n'))
    _, _, text_blob = next(chapter_iter)
    tokens = ttt.tokenize(text_blob)
    for token in tokens:
        paragraph = token.replace("\n", " ")
        print(paragraph)
        print("\n") 
