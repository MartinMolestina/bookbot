from stats import num_words, char_count, sort_dict
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:

        path = sys.argv[1]

        words = num_words(path)

        char_dict = char_count(path)

        sorted_dict = sort_dict(char_dict)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {words} total words")
        print("--------- Character Count -------")

        for e in sorted_dict:
            if e.isalpha():
                print(f"{e}: {sorted_dict[e]}")

        print("============= END ===============")

if __name__ == "__main__":
    main()
