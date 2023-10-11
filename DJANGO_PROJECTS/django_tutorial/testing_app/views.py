from django.shortcuts import render

def home_view(request):
    return render(request, '/home/dci-student/Class_FbW_P23_e02/FRAMEWORK/DJANGO_PROJECTS/django_tutorial/testing_app/templates/home.html', {"message": "Welcome to the homepage!"})

def about_view(request):
    return render(request, '/home/dci-student/Class_FbW_P23_e02/FRAMEWORK/DJANGO_PROJECTS/django_tutorial/testing_app/templates/about.html', {"message": "About us page."})
