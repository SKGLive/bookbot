def count_words(book_contents):
    # Take in string and count number of words within string
    count = 0
    for word in book_contents.split():
        count += 1
    return count

def count_characters(book_contents):
    # Take in string and count number of characters within string
    # returns the number of times each character(including symbols and spaces) appears

    char_dict = {}
    for char in book_contents.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_dict(_dict):
    sorted_list = dict(sorted(_dict.items(), key=lambda item: item[1], reverse=True))
    #print(sorted_list)
    return sorted_list