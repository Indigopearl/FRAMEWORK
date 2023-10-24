# books/urls.py
from django.urls import path
from django.views.generic import TemplateView
from .views import (
    BookListView,
    BookDetailView,
    BookUpdateView,
    BookCreateView,
    BookDeleteView,
)

app_name = "books"

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("books/", BookListView.as_view(), name="book_list"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("book/new/", BookCreateView.as_view(), name="book_create"),
    path("book/<int:pk>/edit/", BookUpdateView.as_view(), name="book_edit"),
    path("book/<int:pk>/delete/", BookDeleteView.as_view(), name="book_delete"),
]
