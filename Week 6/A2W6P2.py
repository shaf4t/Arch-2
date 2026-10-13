def search_book(books: list[dict[str, str]], term: str) -> bool:
    search_term = term.strip().lower()
    return any(
        search_term in book[field].lower()
        for book in books
        for field in ("title", "author", "publisher")
    )


def add_book(books: list[dict[str, str]], details: str) -> bool:
    values = [value.strip() for value in details.split(",")]
    if len(values) != 4 or not all(values):
        return False

    title, author, publisher, pub_date = values
    if any(book["title"].lower() == title.lower() for book in books):
        return False

    books.append(
        {
            "title": title,
            "author": author,
            "publisher": publisher,
            "pub_date": pub_date,
        }
    )
    return True


def main() -> None:
    books = []

    while True:
        print("[A] Add book [S] Search book [E] Exit (and print)")
        choice = input("Choice: ").strip().lower()

        if choice == "a":
            details = input("Book details: ")
            if add_book(books, details):
                print("Book has been added")
            else:
                print("Book could not be added")
        elif choice == "s":
            term = input("Search term: ")
            if search_book(books, term):
                print(f"Found a book for: {term}")
            else:
                print(f"No book found for: {term}")
        elif choice == "e":
            for book in books:
                print(book)
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()