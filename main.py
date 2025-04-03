from stats import num_words, char_count, sort_dict


def main():
    frankenstein_path = "./books/frankenstein.txt"

    words = num_words(frankenstein_path)

    print(f"{words} words found in the document")

    char_dict = char_count(frankenstein_path)

    sorted_dict = sort_dict(char_dict)

    for e in sorted_dict:
        if e.isalpha():
            print(f"{e}: {sorted_dict[e]}")

if __name__ == "__main__":
    main()
