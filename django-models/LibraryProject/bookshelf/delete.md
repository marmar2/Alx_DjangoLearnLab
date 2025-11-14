
from bookshelf.models import Book

book = Book.objects.filter(title="1984")


book.delete()

book = Book.objects.get(title="1984")

print(book.title,book.author,book.publication_year)


<!--  -->