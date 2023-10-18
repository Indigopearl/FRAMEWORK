from django.http import HttpResponseForbidden
from django.views.generic import ListView
from .models import Item


class UserAuthMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_superuser:
            return HttpResponseForbidden("You don't have permission to view this page.")
        return super().dispatch(request, *args, **kwargs)


from django.views.generic import TemplateView


class ProtectedView(UserAuthMixin, TemplateView):
    template_name = "protected.html"


class ItemListView(ListView):
    model = Item
    template_name = "item_list.html"
    context_object_name = "items"
