from django.urls import path
from . import views

urlpatterns = [
    # URL for displaying the list of all movies
    path('movies/', views.movie_list, name='movie_list'),

    # URL for viewing the details of a specific movie, using a dynamic parameter 'movie_id'
    path('movie/<int:movie_id>/', views.movie_details, name='movie_details'),

    # URL for searching for movies, using a query parameter 'title'
    path('search/', views.search_movies, name='search_movies'),
]
