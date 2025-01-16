def open_book(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(input):
    words = input.split()
    return len(words)

def count_characters(input):
    input_lowercase = input.lower()
    letters_dict  = {}
    for char in input_lowercase:
        if char not in letters_dict:
            letters_dict[char] = 1
        else:
            letters_dict[char] += 1
    return letters_dict


def main():
    book_path = "books/frankenstein.txt"
    text = open_book(book_path)
    word_count = count_words(text)
    char_count = count_characters(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    char_list = []
    for char in char_count:
        if char.isalpha():
            char_dict = {"letter": char, "count": char_count[char]}
            char_list.append(char_dict)
    def sort_on(dict):
        return dict["count"]
    char_list.sort(reverse=True, key=sort_on)
    for char in char_list:
        print(f"The character {char["letter"]} was found {char["count"]} times")

    
    #print(char_list)

    
    print("--- End report ---")

main()

