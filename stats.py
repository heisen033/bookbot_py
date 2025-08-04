def get_number_of_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        string_list = file_contents.split()
        print(f"Found {len(string_list)} total words")


def get_number_of_each_char(filepath):
    char_dict = {}
    with open(filepath) as f:
        file_contents = f.read()
        for char in file_contents:
            if char.lower() in char_dict:
                char_dict[char.lower()] += 1
            else:
                char_dict[char.lower()] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort_dict_by_number(char_dict):
    list_of_chardicts = []
    for char in char_dict:
        single_char_dict = {
            "char": char, "num": char_dict[char]
        }
        list_of_chardicts.append(single_char_dict)
    list_of_chardicts.sort(reverse=True, key=sort_on)
    return list_of_chardicts

def report(filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...\n"
    "----------- Word Count ----------")
    get_number_of_words(filepath)
    print("--------- Character Count -------")
    list_of_chardicts = sort_dict_by_number(get_number_of_each_char(filepath))
    for item in list_of_chardicts:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
        