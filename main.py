from stats import get_book_text, char_freq, sorted_dict
import sys


def main():
    try:
        b_text = get_book_text(sys.argv[1]).split()
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    count = 0
    for word in b_text:
        count += 1
    print(f"Found {count} total words")
    for key, value in sorted_dict(char_freq(b_text)):
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
