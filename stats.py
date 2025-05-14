def sort_on(dict):
    return dict["num"]

def word_count(text):
    num_words = len(text.split())
    return num_words

def char_count(text):
    text = text.lower()
    characters = list(text)
    char_dict = {}
    for character in characters:
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1
    return char_dict


def char_report(text):
    sorted_char_list = []
    for k, v in char_count(text).items():
        dict = {}
        dict["char"] = k
        dict["num"] = v
        sorted_char_list.append(dict)
        sorted_char_list.sort(reverse=True, key=sort_on)
        
    for char in sorted_char_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")