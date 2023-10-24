from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponse
from django.views import View

class SignUpView(CreateView):
    success_url = reverse_lazy("login")
    template_name = 'signup.html'

    form_class = UserCreationForm

class SessionKeyExample(View):

    def get(self, request, *args, **kwargs):
        # Check if session_key is already set
        if request.session.session_key:
            response_text = f"Welcome back! Session key: {request.session.session_key}"
        else:
            request.session['example_data'] = 'THis is some sessiom data'
            response_text = "Welcome!"
        response = HttpResponse(response_text)
        # response.set_cookie('my_cookie', 'value')
        csrf_token = request.COOKIES['csrftoken']
        response.set_cookie('csrftoke', csrf_token + 'bla')
        
        return response

