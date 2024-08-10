from models import Book, User, Author

books = []
users = []
authors = []

def add_book(title, author, genre, publication_date):
    book = Book(title, author, genre, publication_date)
    books.append(book)
    print("Book added successfully!")

def borrow_book(title, user_library_id):
    book = next((b for b in books if b.title == title and b.availability), None)
    user = next((u for u in users if u.library_id == user_library_id), None)
    if book and user:
        book.availability = False
        user.borrow_book(title)
        print(f"Book '{title}' borrowed by user with ID {user_library_id}.")
    else:
        print("Book or User not found, or Book is not available.")

def return_book(title, user_library_id):
    book = next((b for b in books if b.title == title), None)
    user = next((u for u in users if u.library_id == user_library_id), None)
    if book and user:
        book.availability = True
        user.return_book(title)
        print(f"Book '{title}' returned by user with ID {user_library_id}.")
    else:
        print("Book or User not found.")

def search_book(title):
    book = next((b for b in books if b.title == title), None)
    if book:
        print(book)
    else:
        print("Book not found.")

def display_all_books():
    for book in books:
        print(book)

def add_user(name, library_id):
    user = User(name, library_id)
    users.append(user)
    print("User added successfully!")

def view_user_details(library_id):
    user = next((u for u in users if u.library_id == library_id), None)
    if user:
        print(user)
    else:
        print("User not found.")

def display_all_users():
    for user in users:
        print(user)

def add_author(name, biography):
    author = Author(name, biography)
    authors.append(author)
    print("Author added successfully!")

def view_author_details(name):
    author = next((a for a in authors if a.name == name), None)
    if author:
        print(author)
    else:
        print("Author not found.")

def display_all_authors():
    for author in authors:
        print(author)
