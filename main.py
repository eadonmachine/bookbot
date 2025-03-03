import sys
from stats import count_words, count_characters, sort_characters

def open_book(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = open_book(book_path)
    word_count = count_words(text)
    char_count = count_characters(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    sorted_list = sort_characters(char_count)
    for char in sorted_list:
        print(f"{char["letter"]}: {char["count"]}")
    print("============= END ===============")

main()

