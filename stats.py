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
