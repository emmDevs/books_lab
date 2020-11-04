import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Frances", "Hodgson")
author2 = Author("JK", "Rowling")
book1 = Book("The secret garden", "fiction", "Penguin", author1)
book2 = Book("Harry Potter", "fiction", "Ladybird", author2 )

author_repository.save(author1)
book_repository.save(book1)
author_repository.save(author2)
book_repository.save(book2)

pdb.set_trace()

