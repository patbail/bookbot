from stats import *
import sys
arg = sys.argv
filepath = ""

if len(arg) >= 2:
    filepath = arg[1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    return filepath.read()

def main():
    with open(filepath) as f:
        book_text = get_book_text(f)
        # print(book_text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count(book_text)} total words")
        print("--------- Character Count -------")
        char_report(book_text)
        print("============= END ===============")

main()