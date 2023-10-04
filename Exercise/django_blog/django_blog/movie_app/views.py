from django.shortcuts import render
from .models import Movie


def movie_list(request):
    # Retrieve all movies from the database
    movies = Movie.objects.all()

    # Render the 'movie_list.html' template with the list of movies
    return render(request, 'movie_app/movie_list.html', {'movies': movies})


def movie_details(request, movie_id):
    # Retrieve the movie with the specified movie_id from the database
    movie = Movie.objects.get(id=movie_id)

    # Render the 'movie_details.html' template with the movie details
    return render(request, 'movie_app/movie_details.html', {'movie': movie})


def search_movies(request):
    # Get the search query from the URL's GET parameters
    search_query = request.GET.get('title', '')

    # Perform a case-insensitive search for movies containing the search query in their title or genre
    movies = Movie.objects.filter(title__icontains=search_query) | Movie.objects.filter(
        genre__icontains=search_query)

    # Render the 'movie_search_results.html' template with the search results
    return render(request, 'movie_app/movie_search_results.html', {'movies': movies, 'search_query': search_query})
