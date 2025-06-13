from stats import get_book_text, char_freq, sorted_dict, sorted_on


def main():
    b_text = get_book_text("frankenstein.txt").split()
    count = 0
    for word in b_text:
        count += 1
    print(sorted_dict(char_freq(b_text)))


if __name__ == "__main__":
    main()
