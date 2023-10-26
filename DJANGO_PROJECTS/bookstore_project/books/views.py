from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Book
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseForbidden

class HomeView(TemplateView):
    template_name = 'home.html'

def home(request):
    return render(request, 'home.html')

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'description', 'published_date', 'price']
    success_url = reverse_lazy('books:book_list')
    
    # Specify the required permission (change this to your actual permission)
    permission_required = 'your_app.change_book'

    def handle_no_permission(self):
        # Return a 403 Forbidden response when the user doesn't have the required permission
        return HttpResponseForbidden()

class BookCreateView(CreateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'description', 'published_date', 'price']
    success_url = reverse_lazy('books:book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('books:book_list')
