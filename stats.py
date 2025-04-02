

# open a document and count the numer of words in it
def num_words(path):
    with open(path) as f:
        text = f.read()

    words = len(text.split())
    return words
