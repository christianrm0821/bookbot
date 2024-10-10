def main():
    book_path = "books/frankenstein.txt"
    word_count = get_word_count(book_path)
    char_count = get_character_count(book_path)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    for key, value in char_count.items():
        print(f"The '{key}' character was found {value} times")
    print("--- End of Report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(path):
    text = get_book_text(path)
    words = text.split()
    return len(words)

def get_character_count(path):
    text = get_book_text(path)
    char_count = {}
    tmp = 'abcdefghijklmnopqrstuvwxyz'
    for c in tmp:
        char_count[c]=0
    text = text.lower()
    for x in text:
        if x in tmp:
            char_count[x] +=1
    return char_count

main()