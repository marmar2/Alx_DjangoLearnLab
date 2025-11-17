from django.urls import path
from . import views
from .views import list_books, LibraryDetailView,register,LoginView,LogoutView,admin_view




urlpatterns = [
    path('books/', views.list_books, name="list_books" ),
    path('library/', views.LibraryDetailView.as_view(), name='Lib details'),
    path('register/',views.register, name="register" ),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'),name="login" ),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'),name="logout" ),
    path('admin/', admin_view, name='admin_view'),
]

    