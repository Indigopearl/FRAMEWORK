from django.shortcuts import render
from .models import Books


def book_list(request):
    books = Books.objects.all()
    return render(request, 'book_list.html', {'books': books})
