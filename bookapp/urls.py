from django.urls import path
from bookapp import views
import bookapp

urlpatterns = [
    path('',views.book,name='home'),
    path('add/',views.addbook, name='add'),
    path('list/',views.listbook, name='list'),
    path('search/',views.search, name='search'),
    
]