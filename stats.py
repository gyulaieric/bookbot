def get_word_count(book):
    return len(book.split())

def get_character_count(book):
    result = {}
    book = book.lower()

    for char in book:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result

def sort_character_dictionary(dict):
    list = []

    def sort_on(items):
        return items["num"]

    for key in dict:
        list.append({"char": key, "num": dict[key]})

    list.sort(reverse=True, key=sort_on)

    return list