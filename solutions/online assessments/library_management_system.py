"""
Design a library management system that stores Books with a title, genre and rating (float)

The system will have the following functions
- Adding a book to the system
- Getting the x number of highest rated books
- Getting the highest rated book for the specified genre
"""

import heapq

class Book:
    def __init__(self, title, genre, rating):
        # Write code here
        self.title = title
        self.genre = genre
        self.rating = rating  # float
   
class LibraryManagement:
    def __init__(self):
        # Write code here
        self.books = []
        self.books_genre = {}
   
    def add_book(self, book):
        # Write code here
        self.books.append(book)
        
        if book.genre not in self.books_genre:
            self.books_genre[book.genre] = []
        self.books_genre[book.genre].append(book)
            
    # returns x highest rated books
    def get_highest_rated_books(self, x):
        # Write code here
        top_books = heapq.nlargest(x, self.books, key=lambda book: book.rating)
        return top_books
    
    # returns highest rated book in genre
    def recommend_top_book_by_genre(self, genre):
        # Write code here
        if genre in self.books_genre and self.books_genre[genre]:
            return max(self.books_genre[genre], key=lambda book: book.rating)
        return None