from django.db import models

# Create your models here.
class Book(models.Model):

    bookname = models.CharField( max_length=50)
    author = models.CharField( max_length=50)  
    genre = models.CharField( max_length=50)
    language = models.CharField(max_length=50)

    def __str__(self):

        return self.bookname
