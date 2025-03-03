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

def sort_characters(char_count):
    char_list = []
    for char in char_count:
        if char.isalpha():
            char_dict = {"letter": char, "count": char_count[char]}
            char_list.append(char_dict)
    def sort_on(dict):
        return dict["count"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list
