from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, resolve

class SpecialUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        user_id = request.session.get('_auth_user_id')
        if user_id:
            user = User.objects.get(pk=user_id)
            return HttpResponse(f"You are user {user}!")

        response = self.get_response(request)
     
        print(response)
        response.write('Hello world')

         
        return response

class ProtectSpecificRoutesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # List of protected URL names
        protected_url_names = [
            'home',
            'post_new',
            'post_edit',
            'post_delete',
        ]

        # Resolve the curren path to its URL name
        try:
            current_url_name = resolve(request.path_info).url_name
        except:
            current_url_name = None

        if current_url_name in protected_url_names and not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))

        return self.get_response(request)