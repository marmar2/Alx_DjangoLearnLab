

books = Book.objects.all()

for i in books:print(i.title,i.author,i.publication_year)

print(newBook.title,newBook.author,newBook.publication_year)

newBook.delete()

books = Book.objects.all()

for i in books:print(i.title,i.author,i.publication_year)


<!--  -->