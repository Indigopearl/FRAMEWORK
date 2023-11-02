from rest_framework.generics import ListAPIView
from .models import Plant
from .serializers import PlantSerializer
from django.views.generic import ListView
from rest_framework import renderers

class PlantListView(ListView):
    model = Plant
    template_name = "plants/plant_list.html"
    context_object_name = "plants"

class PlantListAPI(ListAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
