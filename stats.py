def get_book_text(bookname):
    with open(f"/Users/kronos/workspaces/github.com/AzharAhmad1996/bookbot/{bookname}") as b:
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

def sorted_dict(t_dict):
    return sorted(t_dict.items(),reverse=True, key=lambda item : item[1])
