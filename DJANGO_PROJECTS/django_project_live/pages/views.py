from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

def home2PageView(request):
    context = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'Hello',
        'first': [1, 2, 3],
        'second': [4, 5, 6],
        'today': datetime.now()
    }
    return render(request, 'home2.html', context)
