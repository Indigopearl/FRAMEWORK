from django.shortcuts import redirect

def protected_view(request):
    if not request.user.is_authenticated:
        # Store the current page's URL in the session
        request.session['previous_page'] = request.get_full_path()
        return redirect('login')  # Redirect to the login page
    # Your protected view logic here
