from relationship_app.models import Book,Librarian,Library,Author


library_name = Library.objects.get(name="libraryxx")
libraryName = Library.objects.get(name=library_name)              
ListOfBooks = libraryName.books.all()   # books is related_name in class library , that has library and book mapping

#Query all books by a specific author.
author_name = Author.objects.get(name='authorxx')
ListOfBooks_specificAuthor = Book.objects.filter(author=author_name)

librarianName = Librarian.objects.get(library__name='hh')

# ORR
# library = Library.objects.get(name="librarian") --- > reverse query librarian (related name) is a foreign key in Library
