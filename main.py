def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    dictionary = count_char(file_contents)
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")
    for char in alphabet:
        if char.isalpha():
            print(f"The {char} character was found {dictionary[char]} times")
    print("--- End report ---")


def count_words(text):
    cnt = 0
    for _ in text.split():
        cnt += 1
    return cnt


def count_char(text):
    dictionary = {}
    unique = []

    for char in text.lower():
        if char in unique:
            dictionary[char] += 1
        if char not in unique:
            dictionary[char] = 1
            unique.append(char)
    return dictionary


if __name__ == '__main__':
    main()
    