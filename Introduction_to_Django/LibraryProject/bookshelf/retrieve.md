book = Book.objects.get(title="1984")

books = Book.objects.all()

for i in books:print(i.title,i.author,i.publication_year)

<!-- 1984 George Orwell 1949 -->