# Topic:

- user accounts
- user signin, logout
- sessions
- middleware

# User Accounts

 So far, we've built a working Blog application with forms but still need a major piece of most web applications: 
**user authentication**.

Implementing proper user authentication is famously hard; there are many security gotchas along the way, so you don’t want to implement this yourself.

Fortunately, Django has a powerful, built-in user authentication system that we can use and customize as needed.

Whenever you create a new project, by default, Django installs the **auth app**, which provides us with a User object containing:

- username
- password
- email
- first_name
- last_name

We will use this User object to implement login, logout, and signup in our blog application.

### Log In

Django provides us with a default view for a login page via LoginView. 

All we need to add are 

- a URL pattern for the auth system,
- a login template, and 
- a minor update to our django_project/settings.py file.

First, update the django_project/urls.py file. 

We'll place our login and logout pages at the accounts/ URL:

```python
# django_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")), # new
    path("", include("blog.urls")),
]
```

As the LoginView documentation notes 
(https://docs.djangoproject.com/en/4.2/topics/auth/default/#django.contrib.auth.views.LoginView),

by default Django will look within a templates directory called registration for a file called login.htm1l for
a login form.

So we need to create a new directory called registration and the requisite file within it. From the command line, type Control+c to quit
our local server. Then create the new directory.

```Shell
(.venv) $ mkdir templates/registration
```

And then, with your text editor, create a new template file, templates/registration/login.html, filled with the following code:

```html
<!-- templates/registration/login.html -->
{% extends "base.html" %}
{% block content %}

<h2>Log In</h2>
<form method="post">{% csrf_token %}

{{ form.as_p }}

<button type="submit">Log In</button>
</form>
{% endblock content %}
```

We're using HTML <form></form> tags and specifying the POST method since we're sending data to the server (we’d use GET if we were requesting data, such asin a search engine form). 

We add {% csrf_token %} for security concerns to prevent a CSRF Attack. The form’s contents are outputted between
paragraph tags thanks to {{ form.as_p }} and then we add a “submit” button.

The final step is to specify where to redirect the user upon successful login.
 We can set this with the LOGIN_REDIRECT_URL setting. 

 At the bottom of the django_project/settings.py file, add the following:

 ```python
# django_project/settings.py
LOGIN_REDIRECT_URL = "home" # new
```

Now the user will be redirected to the 'home ' template, which is our homepage.

Upon entering the login info for our superuser account, we are redirected to the homepage.

Notice that we didn’t add any view logic or create a database model because the Django auth system provided both for us automatically. 

### Updated Homepage

Let’s update our base.html template so we display a message to users whether they are logged in or not. We can use the is_authenticated attribute for this.

Update the base.html file with new code:

```html
<!-- templates/base.html -->
{% load static %}
<html>
<head> 3
<title>Django blog</title>
<link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400" 3
rel="stylesheet"> |
<link href="{% static 'css/base.css' %}" rel="stylesheet" s> 3
</head>
<body> i
<div> :
<header> 3
<div class="nav-left"> 3
<h1><a href="{% url 'home' %}">Django blog</a></h1>

</div>

<div class="nav-right">

<a href="{% url 'post_new' %}">+ New Blog Post</a>

</div>
</header>
<!-- start new HTML... -->

{% if user.is_authenticated %} 
<p>Hi {{ user.username }}!</p> 

{% else %}
<p>You are not logged in.</p>
<a href="{% url 'login' %}">Log In</a>
{% endif %}
<!-- end new HIML... -->
{% block content %}
{% endblock content %}
</div>
</body>
</html>
```

If the user is logged in, we say hello to them by name; if not, we provide a link to our newly created login page.


### Log Out Link

We added template page logic for logged-out users, but how do we log out now?

We could go into the Admin panel and do it manually, but there’s a better way. 
Let’s add a logout link instead that redirects to the homepage.
Thanks to the Django auth system, this is dead simple to achieve.

In our base.html file,add a one-line {% url 'logout' %} link for logging out just below our user greeting.

```html
<!-- templates/base.html-->
{% if user.is_authenticated %} 3
<p>Hi {{ user.username }}!</p>
<p><a href="{% url 'logout' %}">Log out</a></p>
{% else %}
```

The Django auth app provides us with the necessary view so all we need to do is specify where to redirect a user upon logging out. 

Update django_project/settings.py to provide a redirect link called, appropriately, LOGOUT_REDIRECT_URL:

```python
# django_project/settings.py
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT URL = "home" # new
```

If you refresh the homepage, you'll see it now has a “log out” link for logged-in users.

### Sign Up

We need to write our own view for a signup page to register new users, but Django does provide us with a form class, UserCreationForm, to make things easier.

By default, it comes with three fields: username, password1, and password2.

There are many ways to organize your code and URL structure for a robust user authentication system.

Stop the local server with Control+c and create
a dedicated new app, accounts, for our signup page.

```Shell
(.venv) $ python manage.py startapp accounts
```

Add the new app to the INSTALLED_APPS setting in our django_project/settings.py file.
```python
# django_project/settings.py
INSTALLED_APPS = [
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib.sessions",
"django.contrib.messages",
"django.contrib.staticfiles",
"blog",
"accounts", # new
]
```

Next, add a new URL path in django_project/urls.py pointing to this new app directly below where we include the built-in auth app.

```python
# django_project/urls.py
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
path("admin/", admin.site.urls),
path("accounts/", include("django.contrib.auth.urls")),
path("accounts/", include("accounts.urls")), # new
path("", include("blog.urls")),
]
```
The order of our urls matters here because Django reads this file from top to bottom. 

Therefore when we request the /accounts/signup url, Django
will first look in auth, not find it, and then proceed to the accounts app.

create a file called accounts/urls.py and add the following code:

```python
# accounts/urls.py
from django.urls import path
from .views import SignUpView

urlpatterns = [
path("signup/", SignUpView.as_view(), name="signup"),
]

```

We're using a view called SignUpView, which we already know is class-based since it is capitalized and has the as_view() suffix. 

Its path is just signup/, so the complete URL path will be accounts/signup/.

Now for the view, which uses the built-in UserCreationForm and generic CreateView. 

Replace the default accounts/views.py code with the
following:

```python
# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
class SignUpView(CreateView):

form_class = UserCreationForm

success_url = reverse_lazy("login")

template_name = "signup.html"
```

- We’re subclassing the generic class-based view CreateView 
- specify UserCreationForm
- specify the template signup.html.


Why use reverse_lazy here instead of reverse?

The reason is that the URLs are not loaded when the file is imported for generic class-based views,
so we have to use the lazy form of reverse to load them later when they're available.

create the file signup.html within the templates/ directory:

``html
<!-- templates/registration/signup.html -->
{% extends "base.html" %}
{% block content %}
<h2>Sign Up</h2>
<form method="post">{% csrf_token %}

{{ form.as_p }}

<button type="submit">Sign Up</button>
</form>
{% endblock content %}
```

This format is very similar to what we’ve done before. 

We extend our base template at the top, place our logic between <form></form> tags, use the
csrf_token for security, display the form’s content in paragraph tags with form. as_p, and include a submit button.

Notice how there is a lot of extra text that Django includes by default.

I've created a new user called "john_snow" and, upon submission, was redirected to the login page.

Then after logging in successfully with my new username
and password, I was redirected to the homepage with our personalized “Hi username” greeting.

Our ultimate flow is, therefore: Signup -> Login -> Homepage. 

And, of course, we can tweak this however we want. The SignUpView redirects to login because we set 
success_url = reverse_lazy('login').


### Sign Up Link

One last improvement we can make is to add a signup link to the logged-out homepage. We can’t expect our users to know the correct URL after all! 

How do we do this? 

Well, we need to figure out the URL name, and then we can pop it into our template. 

In accounts/urls.py, we provided it the name of signup, so that’s all we need to add to our base.html template with the url template tag just as we’ve done for our other links.

Add the link for “Sign Up” just below the existing link for “Log In” as follows:

``html
<!-- templates/base.html-->
<p>You are not logged in.</p>
<a href="{% url 'login' %}">Log In</a> 
<a href="{% url 'signup' %}">Sign Up</a>
```

If you refresh the logged-out homepage, the signup link is now visible.


## Web Sessions

**1. Requests are Stateless:**

In the world of web technologies, the HTTP protocol, which forms the foundation of data communication on the World Wide Web, is stateless. 

This means that each request from a client to a server is treated as an isolated transaction with no memory of previous requests. 

From the perspective of the server, every request is a new one, without any context from prior interactions.

**2. Web Sessions:**

Because HTTP is stateless, there arose a need to maintain some **sort of state** during user interactions on websites, especially for scenarios like online shopping, logging into user accounts, etc.

This is where web sessions come into play.

A web session is a mechanism used to store user-specific information on the server side during multiple request-response interactions.

Sessions can be implemented in various ways, like using cookies, hidden form fields, and server-side session management. 

The purpose is to give the user a continuous experience, as if the server "remembers" them, even though HTTP by nature does not.

**3. User and State:**

The "state" refers to any data or information about that user's interaction that we want to maintain across multiple requests.

This state can include things like login status, items added to a shopping cart, user preferences, and more.

--> while HTTP requests are inherently stateless, web sessions provide a way to maintain state across multiple interactions, ensuring a seamless user experience.


#### Session Data with Django

Django does all the hard work of managing session ids.

The session property of the request object in views can be used to get and set the data.



