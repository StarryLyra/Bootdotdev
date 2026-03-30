from stats import number_of_words, number_of_characters, dict_characters
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analizing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words(text)} total words")
    print("--------- Character Count -------")
    print(f"{dict_characters(text)}")
    #print(f"{number_of_characters(text)}")



main()
print(sys.argv)