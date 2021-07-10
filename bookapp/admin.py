from django.contrib import admin
from django.urls.conf import include
from .models import Book
# Register your models here.
admin.site.register(Book)