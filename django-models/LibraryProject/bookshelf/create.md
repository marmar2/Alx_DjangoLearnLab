<!-- newBook = Book(title='1984',author='George Orwell',publication_year=1949)

newBook.save() -->


newBook = Book.objects.create(title='1984',author='George Orwell',publication_year=1949)

book = Book.objects.get(title = '1984')

print(book.title,book.author,book.publication_year)

<!-- 1984 George Orwell 1949 -->