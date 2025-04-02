from stats import num_words




def main():
    frankenstein_path = "./books/frankenstein.txt"

    words = num_words(frankenstein_path)

    print(f"{words} words found in the document")

if __name__ == "__main__":
    main()
