from django.db import models
from django.contrib.auth.models import User
from .models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200,default='hii')
    
    def __str__(self):
        return self.name  # Shows author name in admin and shell

class Book(models.Model):
    title = models.CharField(max_length=200, default='hii')
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name="author")
    
    def __str__(self):
        return self.author  

class Library(models.Model):
    name = models.CharField(max_length=200,default='hii')
    books = models.ManyToManyField(Book,related_name="books")

    def __str__(self):
        return self.name 
    

class Librarian(models.Model):
    name = models.CharField(max_length=200,default='hii')
    library = models.OneToOneField(Library,on_delete=models.CASCADE,related_name="librarian")
      
        
    def __str__(self):
        return self.name   
    
    

class UserProfile(models.Model):
    
    ROLE_CHOICES = [   #Tuple
    ('admin', 'Admin'),
    ('librarian', 'Librarian'),
    ('member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='admin')


@receiver(post_save, sender=User)
def createUserProfile (sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)