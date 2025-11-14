from django.shortcuts import render
from .models import Book , Librarian, Author
from .models import Library
from django.http import HttpResponse
from django.views.generic.detail import DetailView


# Create your views here.

#This view should render a simple text list of book titles and their authors.
def list_books(request):
    books = Book.objects.all()
    book_list = {'books' : books}

    return render(request, 'relationship_app/list_books.html',book_list )


#Create a class-based view in relationship_app/views.py that displays details for a specific library, listing all books available in that library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    
    def get_context_data(self, **kwargs):
        contextDictionary = super().get_context_data(**kwargs) # default dict value
        library = self.get_object()
        contextDictionary['bookList'] = library.books.all()
        return contextDictionary


    