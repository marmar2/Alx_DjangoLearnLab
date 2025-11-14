from django.shortcuts import render
from .models import Book , Librarian, Author
from .models import Library
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic import CreateView
from django.urls import reverse_lazy



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

def register(request):
     form = UserCreationForm(request.POST or None)  # instantiate for POST or empty for GET
     if form.is_valid():  # only save if form passes validation
         user = form.save()
         login(request, user)
     success_url = reverse_lazy('login')
     
     return render(request, 'relationship_app/register.html', {'form': form})

# class  register(CreateView):
#     form_class = UserCreationForm()
#     success_url = reverse_lazy('login')
#     template_name = 'relationship_app/register.html'

#     def form_valid(self, form):
#         response =  super().form_valid(form)
#         login(self.request, self.object) #automatically logs in the new user right after signup
#         return response


