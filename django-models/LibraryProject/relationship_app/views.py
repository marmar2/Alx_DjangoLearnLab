from django.shortcuts import render
from relationship_app.models import Book , Librarian, Library, Author
from django.http import HttpResponse
from django.views.generic import DetailView


# Create your views here.

#This view should render a simple text list of book titles and their authors.
def book_list(request):
    books = Book.objects.all()
    book_list = {'books' : books}

    return render(request, 'relationship_app/list_books.html',book_list )

class LibraryDetails(DetailView):
    model = Library
    template_name = 'relationship_app/list_books.html'
    
    def get_context_data(self, **kwargs):
        contextDictionary = super().get_context_data(**kwargs) # default dict value
        library = self.get_object()
        contextDictionary['bookList'] = library.books.all()
        return contextDictionary


    