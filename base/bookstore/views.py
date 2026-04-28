from django.shortcuts import render
from .models import Books

# Create your views here.


def index(request):
    books = Books.objects.all()
    return render(request, 'books.html', {'books': books})


def single_book(request, book_id):
    book = Books.objects.get(pk=book_id)
    return render(request, 'single_book.html', {'book': book})


def bulgakov(request, author_id):
    books = Books.objects.filter(author_id=author_id)
    return render(request, 'bulgakov.html', {'books': books})