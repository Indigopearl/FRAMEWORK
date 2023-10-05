from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm  # Import the MovieForm you created


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_app/movie_list.html', {'movies': movies})


def movie_details(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movie_app/movie_details.html', {'movie': movie})


def search_movies(request):
    search_query = request.GET.get('title', '')
    movies = Movie.objects.filter(title__icontains=search_query)
    return render(request, 'movie_app/movie_search_results.html', {'movies': movies, 'search_query': search_query})


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_app:movie_list')
    else:
        form = MovieForm()
    return render(request, 'movie_app/add_movie.html', {'form': form})


def remove_movie(request):
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        if movie_id:
            Movie.objects.filter(id=movie_id).delete()
    movies = Movie.objects.all()
    return render(request, 'movie_app/remove_movie.html', {'movies': movies})
