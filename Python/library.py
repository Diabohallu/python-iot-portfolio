
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def describe(self):
        return f"{self.title}\n"


books = []


def add(title, author, isbn):
    for book in books:
        if book.title.lower() == title.lower():
            return f"\n{book.title} already exists"
    books.append(Book(title, author, isbn))
    return f"\nAdded \"{title}\" by {author}. ISBN for {title} is {isbn}."


def take(title):
    for book in books:
        if book.title.lower() == title.lower():
            books.remove(book)
            return f"\nYou have taken {title}."
    return f"\n{title} not found."


def view():
    if not books:
        return "No books available."
    list = ""
    for book in books:
        list += f"{book.describe()}" 
    return list


def search(title):
    for book in books:
        if book.title.lower() == title.lower():
            return f"\n{book.title} is available. ISBN: {book.isbn}"
    return f"\n{title} is not available."

def save():
    with open("library.txt", "a") as file:
        for book in books:
            file.write(f"{book.title} by {book.author}. ISBN for {book.title}: {book.isbn}\n")
    return f"\nLibrary is saved to \"library.txt\""

def load():
    with open("library.txt", "r") as file:
        list = file.read()
        return f"\nBooks saved in \"library.txt\""
        print(list)


print("\n------Welcome to Library------")
print("How can we assist you?")

while True:
    print("\n1. Add a Book")
    print("2. Take a Book")
    print("3. View all Books")
    print("4. Search for a Book")
    print("5. Save Library")
    print("6. Load Library")
    print("7. Exit")

    opt = input("\nWhat would you like to do? ")

    if opt == "1":
        title = input("\nWhich Book would you like to add: ").title().strip()
        author = input(f"Who's the author of {title}: ").title().strip()
        isbn = input(f"Enter the ISBN for {title}: ").strip()
        print(add(title, author, isbn))
    elif opt == "2":
        print("Books you can take:")
        print(view())
        title = input("\nWhich book would you like to take: ").title().strip()
        print(take(title))
    elif opt == "3":
        print("\nList of Books currently available:")
        print(view())
    elif opt == "4":
        title = input("\nWhich book would you like to find: ").title().strip()
        print(search(title))
    elif opt == "5":
        print(save())
    elif opt == "6":
        print(load())
    elif opt == "7":
        print("\nGoodbye\n")
        break
    else:
        print("\nInvalid option, please choose something from the given options")



