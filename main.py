import sys

from stats import get_word_count
from stats import get_character_count
from stats import sort_character_dictionary

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1] 

    print("============ BOOKBOT ============")
    book = get_book_text(path)
    print(f"Analyzing book found at {path}...")

    print("----------- Word Count ----------")
    word_count = get_word_count(book)
    character_count = get_character_count(book)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    for pair in sort_character_dictionary(character_count):
        if(not pair["char"].isalpha()):
            continue

        print(f"{pair["char"]}: {pair["num"]}")
    print("============= END ===============")

main()