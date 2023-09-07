class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, book):
        self.books.remove(book)

    def search_books(self, search_string):
        books_searched = []
        for book in self.books:
            title = book.title.lower()
            author = book.author.lower()
            search = search_string.lower()
            if search in title or search in author:
                books_searched.append(book)
        return books_searched
                
            

# don't touch below this line


def test_library(library_name, book_names, book_authors):
    library = Library(library_name)
    print(f"Created library: {library_name}")
    for i in range(len(book_names)):
        book = Book(book_names[i], book_authors[i])
        library.add_book(book)
        print(f"Added book: {book.title} by {book.author}")
    print(f"Books in {library_name}:")
    for book in library.books:
        print(f"- {book.title} by {book.author}")
    book_to_remove = library.books[0]
    library.remove_book(book_to_remove)
    print(f"Removed book: {book_to_remove.title} by {book_to_remove.author}")
    print("Books in library after removing a book:")
    for book in library.books:
        print(f"- {book.title} by {book.author}")

    # Search for books
    search_query = "kill"
    search_results = library.search_books(search_query)
    if len(search_results) == 0:
        print(f"No results found for search query: {search_query}")
    else:
        print(f"Search results for query '{search_query}':")
        for book in search_results:
            print(f"- {book.title} by {book.author}")


test_library(
    "John's Library",
    ["The Catcher in the Rye", "To Kill a Mockingbird", "1984"],
    ["J.D. Salinger", "Harper Lee", "George Orwell"],
)
test_library(
    "Ashley's Library",
    ["The Great Gatsby", "Pride and Prejudice", "The Lord of the Rings", "Song of Six"],
    ["F. Scott Fitzgerald", "Jane Austen", "J.R.R. Tolkien", "Harper D Kill"],
)
