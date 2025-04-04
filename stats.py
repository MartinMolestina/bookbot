# open file and return string in memory
def open_file(path):
    with open(path) as f:
        return f.read()

# open a document and count the numer of words in it
def num_words(path):
    text = open_file(path)
    words = len(text.split())
    return words

# counts the number of unique characters in a string and returns a dict
def char_count(path):
    char_counts = {}

    text = open_file(path).lower()

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

# sorts the input dictionary by pair values
def sort_dict(char_dict):
    return dict(sorted(char_dict.items(), key=lambda item:item[1], reverse=True))
