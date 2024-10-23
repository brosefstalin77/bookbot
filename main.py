def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_word_count(text)
    characters = get_character_count(text)
    print_report(book_path, words, characters)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

def sort_characters(dict):
    return dict["num"]

def get_character_count(text):
    chars = {}
    text = ''.join(e for e in text if e.isalpha())
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else: 
            chars[lowered] = 1

    list_of_dicts = []
    for key, value in chars.items():
        list_of_dicts.append({"char": key, "num": value})

    sorted_list = sorted(list_of_dicts, reverse=True, key=sort_characters)

    return sorted_list

def print_report(book_path, words, characters):
    print(f"*** Begin report of {book_path} ****")
    print()
    print(f"{words} words found in this document")
    print()
    print("These letters were found this many times:")
    for i in range(len(characters)):
        print(f"The {characters[i]['char']} character was found {characters[i]['num']} times")
    print()
    print("**** End of Report ****")
    print()

main()

