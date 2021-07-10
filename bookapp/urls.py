from django.urls import path
from bookapp import views
import bookapp

urlpatterns = [
    path('',views.book,name='home'),
    path('add/',views.addbook, name='add'),
    path('list/',views.listbook, name='list'),
    path('english/',views.english, name='english'),
    path('hindi/',views.hindi, name='hindi'),
    path('marathi/',views.marathi, name='marathi'),
    path('history/',views.history, name='history'),
    path('romance/',views.romance, name='romance'),
    path('sci/',views.sci, name='sci'),
]