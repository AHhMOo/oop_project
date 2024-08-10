class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__availability = True

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def genre(self):
        return self.__genre

    @property
    def publication_date(self):
        return self.__publication_date

    @property
    def availability(self):
        return self.__availability

    @availability.setter
    def availability(self, status):
        self.__availability = status

    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, Published: {self.__publication_date}, Available: {self.__availability}"

class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    @property
    def name(self):
        return self.__name

    @property
    def library_id(self):
        return self.__library_id

    @property
    def borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book_title):
        self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)

    def __str__(self):
        return f"Name: {self.__name}, Library ID: {self.__library_id}, Borrowed Books: {self.__borrowed_books}"

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    @property
    def name(self):
        return self.__name

    @property
    def biography(self):
        return self.__biography

    def __str__(self):
        return f"Name: {self.__name}, Biography: {self.__biography}"
