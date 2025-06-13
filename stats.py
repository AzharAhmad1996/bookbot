def get_book_text(bookname):
    with open(f"/Users/kronos/workspaces/github.com/AzharAhmad1996/bookbot/books/{bookname}") as b:
        b_contents = b.read()
        return b_contents

def char_freq(text):
    word_freq = {}
    for word in text:
        word = word.lower()
        for letter in word:
            if letter not in word_freq:
                word_freq[letter] = 1
            else:
                word_freq[letter] += 1
    return word_freq

def sorted_on(t_dict):
    return t_dict["name"]

def sorted_dict(t_dict):
    sorted_on(t_dict)
    return t_dict.sort(reverse=True, key=sorted_on)
