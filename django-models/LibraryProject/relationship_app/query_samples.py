from relationship_app.models import Book,Librarian,Library,Author

ListOfBooks_specificAuthor = Book.objects.get(author='dd')

ListOfBooks = Book.objects.all()

librarianName = Librarian.objects.get(library='hh')