
def get_book_text(filepath):
    return filepath.read()

def word_count(text):
    num_words = len(text.split())
    print(f"{num_words} words found in the document")

def main():
    with open("books/frankenstein.txt") as f:
        word_count(get_book_text(f))
        print(get_book_text(f))

main()