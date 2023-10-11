from django.shortcuts import render


def home_view(request):
    return render(request, "home.html", {"message": "Welcome to the homepage!"})


def about_view(request):
    return render(request, "about.html", {"message": "About us page."})
