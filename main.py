import operations as ops
import utils

def main_menu():
    while True:
        print("\nWelcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")

        choice = utils.get_valid_input("Select an option (1-4): ", r"^[1-4]$")
        
        if choice == '1':
            book_operations()
        elif choice == '2':
            user_operations()
        elif choice == '3':
            author_operations()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break

def book_operations():
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to Main Menu")

        choice = utils.get_valid_input("Select an option (1-6): ", r"^[1-6]$")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            publication_date = input("Enter publication date (YYYY-MM-DD): ")
            ops.add_book(title, author, genre, publication_date)
        elif choice == '2':
            title = input("Enter book title to borrow: ")
            user_id = input("Enter user library ID: ")
            ops.borrow_book(title, user_id)
        elif choice == '3':
            title = input("Enter book title to return: ")
            user_id = input("Enter user library ID: ")
            ops.return_book(title, user_id)
        elif choice == '4':
            title = input("Enter book title to search: ")
            ops.search_book(title)
        elif choice == '5':
            ops.display_all_books()
        elif choice == '6':
            break

def user_operations():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to Main Menu")

        choice = utils.get_valid_input("Select an option (1-4): ", r"^[1-4]$")
        
        if choice == '1':
            name = input("Enter user name: ")
            library_id = input("Enter library ID: ")
            ops.add_user(name, library_id)
        elif choice == '2':
            library_id = input("Enter user library ID to view: ")
            ops.view_user_details(library_id)
        elif choice == '3':
            ops.display_all_users()
        elif choice == '4':
            break

def author_operations():
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to Main Menu")

        choice = utils.get_valid_input("Select an option (1-4): ", r"^[1-4]$")
        
        if choice == '1':
            name = input("Enter author name: ")
            biography = input("Enter author biography: ")
            ops.add_author(name, biography)
        elif choice == '2':
            name = input("Enter author name to view: ")
            ops.view_author_details(name)
        elif choice == '3':
            ops.display_all_authors()
        elif choice == '4':
            break

main_menu()
