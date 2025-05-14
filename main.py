from stats import *

def get_book_text(filepath):
    return filepath.read()

def main():
    with open("books/frankenstein.txt") as f:
        book_text = get_book_text(f)
        # print(book_text)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {word_count(book_text)} total words")
        print("--------- Character Count -------")
        char_report(book_text)
        print("============= END ===============")

main()