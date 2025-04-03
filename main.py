from stats import num_words, char_count


def main():
    frankenstein_path = "./books/frankenstein.txt"

    words = num_words(frankenstein_path)

    print(f"{words} words found in the document")

    char_dict = char_count(frankenstein_path)

    print(char_dict)

if __name__ == "__main__":
    main()
