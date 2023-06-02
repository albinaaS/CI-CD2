from django.shortcuts import render
from .models import Book
# Create your views here.
def books_list(request):
    books = Book.Books()
    return render(request, 'book_list.html', context={'books': books})


def book_detail(request, pk):
    book = Book.get_books(pk)
    return render(request, 'book_detail.html', context={'book': book})
