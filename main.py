def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    report(book_path)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    lowered_text = text.lower()
    counts = {}
    for c in lowered_text:
        counts[c] = counts.get(c, 0) + 1
    return counts

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for ch in chars_dict:
        sorted_list.append({"char": ch, "num": chars_dict[ch]})
    sorted_list.sort(reverse=True, key=lambda x: x["num"])

    return sorted_list

def report(path):
    text = get_book_text(path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print()
    for d in chars_sorted_list:
        ch = d["char"]
        num = d["num"]
        if ch.isalpha():
            print(f"The '{ch}' character was found {num} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
