def get_word_count(file_path):
    words = file_path.split()
    word_count = len(words)
    return word_count


def return_character_count(words): 
    character_count = {} 
    lower_case = str.lower(words)
    for l in lower_case:
        if l not in character_count:
            character_count[l] = 1   # start
        else:
            character_count[l] += 1   # increment

    return character_count

def sort_chars_by_count(character_count): # sort dict by numeric value
    chars_list = []
    for char, count in character_count.items():
        chars_list.append({"char": char, "count": count})


    def sort_on(dict_item):
        return dict_item["count"]

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
