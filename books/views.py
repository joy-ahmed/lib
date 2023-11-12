from django.shortcuts import render
from .models import *

# Create your views here.
def books(request):
    books = Book.objects.all()
    return render(request, 'books/books.html', {'books': books})