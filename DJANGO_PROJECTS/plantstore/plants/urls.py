from django.urls import path
from .views import PlantListView, PlantListAPI

app_name = "plants"

urlpatterns = [
    path("", PlantListView.as_view(), name="plant-list"),
    path("api/plants/", PlantListAPI.as_view(), name="plant-list-api"),
]
