from django.db import models

# Create your models here.
lan=(
    ('english','english'),
    ('hindi','hindi'),
    ('marathi','Marathi')
    
)     
gen=(
    ('history','history'),
    ('romance','romance'),
    ('sci_fi','Sci_Fi')
    
)     
class Book(models.Model):
 
    bookname = models.CharField( max_length=50)
    author = models.CharField( max_length=50)  
    genre = models.CharField(choices=gen, max_length=50)
    language = models.CharField(choices=lan,max_length=50)

    def __str__(self):

        return self.bookname
