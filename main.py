from stats import get_num_words
from stats import sortlist
import sys

def get_book_text(pathtofile):
    with open(pathtofile) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    booktext = get_book_text(sys.argv[1])
    number = get_num_words(booktext)
    mycharsorted = sortlist(booktext)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {number} total words")
    print("--------- Character Count -------")
    for item in mycharsorted:
        print(f"{item['char']}: {item['num']}")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()










