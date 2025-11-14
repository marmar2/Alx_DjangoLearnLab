from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField()
    
    def __str__(self):
        return self.name  # Shows author name in admin and shell

class Book(models.Model):
    title = models.CharField(),
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name="Books")


class Library(models.Model):
    name = models.CharField(),
    books = models.ManyToManyField(Book,related_name="libraries")

class Librarian(models.Model):
    name = models.CharField(),
    library = models.OneToOneField(Library,on_delete=models.CASCADE,related_name="librarians")
      