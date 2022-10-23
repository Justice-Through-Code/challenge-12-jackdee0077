
from book import Book


class Library():
    def __init__(self):
        """Initialize the empty book list"""
        self.books = []

    def add_title(self,title,author):
        """Add a Book object with the given title and author to the book list"""
        book = Book(title, author)
        self.books.append(book)

    def count_books(self):
        """Return the number of books currently in the booklist"""
        return len(self.books)

    def remove_title(self):
        """Remove a book from the book list"""
        for novel in self.books:
            if novel.title == title:
                self.books.remove(novel)
            return self.books

    def display_books(self):
        for novel in self.books:
            print(f'{novel.title} -  {novel.author}')


    def is_empty(self):
        """Return True  if the book list is empty, False if not"""
        return self.books == []
