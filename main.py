from stats import count_words, count_characters, sort_dict
import sys

def get_book_text(book):
    book_contents = ""
    with open(book) as f:
        book_contents = f.read()
    return book_contents

def print_report(_dict, _count):
    print("========= BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {_count} total words")
    print("--------- Character Count -------")
    for item in _dict:
        if item.isalpha():
            print(f"{item}: {_dict.get(item)}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    # Get the text of the book
    #print(get_book_text("books/frankenstein.txt"))

    # Print the number of words in the book
    book_contents = get_book_text(book_path)
    num_words = count_words(book_contents)
    #print(f"{num_words} words found in the document")

    # Print the number of characters in the book
    num_characters = count_characters(book_contents)
    #print(num_characters)

    
    sorted_list = sort_dict(num_characters)
    print_report(sorted_list, num_words)
    


main()
