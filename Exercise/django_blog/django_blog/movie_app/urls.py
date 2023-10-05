from django.urls import path
from . import views

app_name = 'movie_app'

urlpatterns = [
    path('movies/', views.movie_list, name='movie_list'),
    path('movie/<int:movie_id>/', views.movie_details, name='movie_details'),
    path('search/', views.search_movies, name='search_movies'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('remove_movie/', views.remove_movie, name='remove_movie'),
]
