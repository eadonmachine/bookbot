from stats import count_words, count_characters

def open_book(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    text = open_book(book_path)
    word_count = count_words(text)
    char_count = count_characters(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_list = []
    for char in char_count:
        if char.isalpha():
            char_dict = {"letter": char, "count": char_count[char]}
            char_list.append(char_dict)
    def sort_on(dict):
        return dict["count"]
    char_list.sort(reverse=True, key=sort_on)
    for char in char_list:
        print(f"{char["letter"]}: {char["count"]}")

    print("============= END ===============")

main()

