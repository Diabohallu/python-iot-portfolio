# Library Management System (without modules)

library = []  # List to store books (each book is a dictionary)

def add_book():
    """Add a new book to the library."""
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    isbn = input("Enter ISBN: ").strip()

    # Check if ISBN is unique
    for book in library:
        if book['isbn'] == isbn:
            print("A book with this ISBN already exists! Please add a unique ISBN.")
            return

    book = {
        "title": title,
        "author": author,
        "isbn": isbn
    }
    library.append(book)
    print("Book added successfully!")

def view_books():
    """Display all books in the library."""
    if not library:
        print("The library is empty.")
    else:
        print("\n--- Book List ---")
        for idx, book in enumerate(library, start=1):
            print(f"{idx}. Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")

def search_book():
    """Search for a book by title."""
    search_title = input("Enter title to search: ").strip().lower()
    found = False
    for book in library:
        if book['title'].lower() == search_title:
            print(f"Found: Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")
            found = True
    if not found:
        print("No book found with that title.")

def save_library():
    """Save the library to a text file."""
    with open("library2.txt", "w") as file:
        for book in library:
            line = f"{book['title']},{book['author']},{book['isbn']}\n"
            file.write(line)
    print("Library saved to file successfully!")

def load_library():
    """Load the library from a text file."""
    try:
        with open("library2.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    book = {
                        "title": parts[0],
                        "author": parts[1],
                        "isbn": parts[2]
                    }
                    library.append(book)
        print("Library loaded from file successfully!")
    except FileNotFoundError:
        print("No saved library file found.")

def main():
    """Main function to run the menu loop."""
    load_library()  # Load data when program starts

    while True:
        print("\n===== LIBRARY SYSTEM =====")
        print("1. Add a Book")
        print("2. View All Books")
        print("3. Search Book by Title")
        print("4. Save Library to File")
        print("5. Load Library from File")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            save_library()
        elif choice == "5":
            load_library()
        elif choice == "6":
            print("Thank you for using the Library System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()