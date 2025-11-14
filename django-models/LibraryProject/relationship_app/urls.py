from django.urls import path
from . import views



urlpatterns = [
    path('books/', views.book_list, name="list_books" ),
    path('library/', views.LibraryDetails.as_view(), name='Lib details'),
]

    