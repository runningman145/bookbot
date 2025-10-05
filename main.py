from stats import count_book_text

def main():
    book_path = "books/frakenstein.txt"
    text = get_book_text(book_path)
    # print(text)

    count_book_text(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
