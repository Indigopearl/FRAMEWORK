from django.http import HttpResponseForbidden


class UserAuthMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_superuser:
            return HttpResponseForbidden("You don't have permission to view this page.")
        return super().dispatch(request, *args, **kwargs)


from django.views.generic import TemplateView


class ProtectedView(UserAuthMixin, TemplateView):
    template_name = "protected.html"
