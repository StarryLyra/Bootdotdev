def number_of_words(text):
    return len(text.split())

def sort_on(text):
    return text["num"]

characters = []

def dict_characters(text):
    char = number_of_characters(text)
    for c in char:
        characters.append({"char": c, "num": char[c]})
    characters.sort(reverse=True, key=sort_on)
    result = ""
    for item in characters:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")

def number_of_characters(text):
    char = {}
    for c in text.lower():
        if c in char:
            char[c] += 1
        else:
            char[c] = 1
    return char