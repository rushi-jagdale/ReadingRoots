from django.shortcuts import redirect, render
from .models import Book
from django.contrib import messages 

# Create your views here.
def book(request):
    return render(request,'index.html')

def addbook(request):
    if request.method == 'POST':
             
        bookname = request.POST['bookname']
        author = request.POST['author']
        genre = request.POST['genre']
        language = request.POST['language']
        
        book = Book.objects.create(bookname=bookname,author=author,genre=genre,language=language)
        book.save()
        messages.info(request, 'New Book Added Successfully')


    return render(request,'addbook.html')    

def listbook(request):
    book = Book.objects.all()
    return render(request,'showbook.html',{'book':book})

# def search(request):
#     query = request.GET['search']
#     data = Book.objects.filter(language=query) | Book.objects.filter(genre=query)
    
#     if data.exists():
#         return render(request,'search.html',{'book':data})
#     else:
#         messages.info(request, 'Result Not Found')
#         return render(request,'search.html')
        

        
def english(request):
    query = Book.objects.filter(language='english')
    if query.exists():
        return render(request,'search.html',{'book':query})

    else:
        messages.info(request, 'Result Not Found')
        return render(request,'search.html')
        

def hindi(request):

    query = Book.objects.filter(language='hindi')
    if query.exists():
        return render(request,'search.html',{'book':query})

    else:
        messages.info(request, 'Result Not Found')
        return render(request,'search.html')

def marathi(request):

    query = Book.objects.filter(language='marathi')
    if query.exists():
        return render(request,'search.html',{'book':query})

    else:
        messages.info(request, 'Result Not Found')
        return render(request,'search.html')

def history(request):

    query = Book.objects.filter(genre='history')
    if query.exists():
        return render(request,'search.html',{'book':query})

    else:
        messages.info(request, 'Result Not Found')
        return render(request,'search.html')        

def romance(request):

    query = Book.objects.filter(genre='romance')
    if query.exists():
        return render(request,'search.html',{'book':query})

    else:
        messages.info(request, 'Result Not Found')
        return render(request,'search.html')                


def sci(request):

    query = Book.objects.filter(genre='sci_fi')
    if query.exists():
        return render(request,'search.html',{'book':query})

    else:
        messages.info(request, 'Result Not Found')
        return render(request,'search.html')                        