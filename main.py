from stats import get_num_words, count, sort_on
import sys

def main(args: list[str]):
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return 0
    book_path = args[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = count(text)
    #print(f"{num_words} words found in the document")
    #print(char_count)
    sorted = sort_on(char_count)
    print(f"""============ BOOKBOT ============
Analyzing book found at [{book_path}]...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for k in sorted:
        print(f"{k[0]}: {k[1]}")
    print("============= END ===============")
    return 0

def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

if __name__ == '__main__':
    from sys import argv, exit
    exit(main(argv))
