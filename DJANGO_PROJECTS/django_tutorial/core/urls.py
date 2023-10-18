from django.urls import path
from .views import ProtectedView, ItemListView

urlpatterns = [
    path("protected/", ProtectedView.as_view(), name="protected"),
    path("items/", ItemListView.as_view(), name="item-list"),
]
