from django.urls import path
from . import views
from .views import list_books



urlpatterns = [
    path('books/', views.list_books, name="list_books" ),
    path('library/', views.LibraryDetails.as_view(), name='Lib details'),
]

    