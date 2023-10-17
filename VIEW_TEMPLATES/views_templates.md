# Pages App

- class based views
- templates
- testing templates

### Initial Set up

- make a new directory for our code called django_project and navigate into it
- create a new virtual environment
- install django
- create a new django project
- create a new app called pages

```bash
mkdir django_projects

cd django_projects

python3.8 -m venv .venv

source .venv/bin/activate

pip install django

pip freeze > requirements.txt

git init

echo '.venv' > .gitignore

django-admin startproject django_project_live .

python manage.py migrate

python manage.py runserver

python manage.py startapp pages
```

## Templates
Every web framework needs a convenient way to generate HTML files
- in Django, the approach is to use templates:
individual HTML files that can be linked together and include basic logic.
Recall that our “Hello, World” site had the phrase hardcoded into a views.py file.
That technically works but does not scale well. 
A better approach is to link a view to a template, thereby separating the information contained in each. 

- create a single project-level templates directory and place all templates within it
- By tweaking our **django_project/settings.py** ﬁle, we can tell Django to look in this directory for templates. 

create a directory called templates:

```bash
mkdir templates
```

file structure (`tree -I '__pycache__'`):

```
.
├── db.sqlite3
├── django_project_live
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── pages
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── requirements.txt
└── templates    
    └── home.html

```

## Class-Based Views 

Early versions of Django only shipped with function-based views, but developers soon found themselves repeating the same patterns over and over.

1. Write a view that lists all objects in a model. 
2. Write a view that displays only one detailed item from a model. 
And so on. 

Generic function-based views were introduced to abstract these patterns and streamline the development of common patterns. 

To help with code reusability, Django added class-based views and generic
class-based views while still retaining function-based views. 

There are three different ways to write a view in Django:

1. function-based
2. class-based
3. generic class-based

- Function-based views are simpler to understand because they mimic the HTTP request/response cycle 
- Class-based views are a little harder to understand because their inheritance structure means you have to dive into the code to see everything happening;

So why bother with generic class-based views?
Once you have used them for
a while, they become elegant and efficient ways to write code.

You can often modify a single method on one to do custom behavior rather than rewriting everything from scratch.
This does, however, come at the cost of complexity. 

When a generic class-based view is not enough, modify it to suit your needs. 

And if that still isn’t enough, revert to a function-based or class-based view. 

In our specific use case, we will use TemplateView (one of the generic views) to display our template.

Replace the default text in the pages/views.py file with the following Code:

## About page

1. add about.html

```
├── db.sqlite3
├── django_project_live
├── manage.py
├── pages
├── requirements.txt
└── templates
    ├── about.html
    └── home.html
```

2. create About view
3. add view to pages/urls

## Extending Templates

The real power of templates is that they can be extended. 

If you think about most websites, the same content appears on every page:
- header, 
- footer, 
- etc.

- Let’s create a base.html file containing a header with links
to our two pages. 
- We could name this file anything, but using base.html

```
└── templates
    ├── about.html
    └── home.html
    └── base.html
```

Django has a minimal templating language for adding links and basic logic in our templates. 
You can see the complete list of built-in template tags
in the official docs. 

Template tags take the form of {% something %} where the “something” is the template tag itself. 

- You can even create custom template tags

- To add URL links in our project, we can use the built-in **url** template tag
which takes the URL pattern name as an argument. 
The url tag uses these names to create links for us automatically.

- The URL route for our homepage is called home.
- To configure a link to it, we use the following syntax:

{% url 'home' %}.

```html
#base.html
<header>
  <a href="{% url 'home' %}">Home</a>
  <a href="{% url 'about' %}">About</a>
</header>

{% block content %} {% endblock content %}
```
At the bottom, we've added a block tag called content.

- Let’s update our home.html and about.html files to extend the base.html template. 
- That means we can reuse the same code from one template in another. 
- The Django templating language comes with an extends method that we can use for this.

```html
#Home
{% extends "base.html" %}


{% block content %}
<h1>Home</h1>
{% endblock content %}
```


```html
{% extends "base.html" %}

{% block content %}
<h1>About</h1>
{% endblock content %}

```

### Built-in template Functions
**add:**
```
{{ value|add:"2" }}
```

if value is 4, then the output will be 6.

This filter will first try to coerce both values to integers.
If this fails, it’ll attempt to add the values together anyway.
This will work on some data types (strings, list, etc.) and fail on others.
If it fails, the result will be an empty string.


For example, if we have:

```
{{ first|add:second }}
```

and first is [1, 2, 3] and second is [4, 5, 6], then the output will be [1, 2, 3, 4, 5, 6].

**lower:**
```
{{ value|lower }}
```
If value is Totally LOVING this Album!, the output will be totally loving this album!.

**date:**

```
{{ value|date:"D d M Y" }}
```
If value is a datetime object (e.g., the result of datetime.datetime.now()), the output will be the string 'Wed 09 Jan 2008'.

## Test

- It’s important to add automated tests and run them whenever a codebase changes
- Tests require a small amount of upfront time to write but more than pay off later on.
- In the words of Django co-creator Jacob Kaplan-Moss, “Code
without tests is broken as designed.”

The Python standard library contains a built-in testing framework called unittest that uses TestCase instances and a long list of assert methods to check for and report failures. 
Django’s testing framework provides several extensions on top of Python’s unittest.TestCase base class.

1. These include a test client for making dummy Web browser requests,
2. several Django-specific additional assertions
3. some test case classes:

1. SimpleTestCase,
2. TestCase, 
3. TransactionTestCase

- Generally speaking, SimpleTestCase is used when a database is unnecessary while TestCase is used when you want to test the database.
- TransactionTestCase is helpful to directly test database transactions

If you look within our pages app, Django already provided a tests.py
file we can use. 
Since no database is involved in our project, we will import
SimpleTestCase at the top of the file. 


For our first tests, we’ll check that the two URLs for our website, the homepage and about page, both return HTTP status codes of 200
(status code 200  is the standard response for a successful HTTP request)

```python
# pages/tests.py
from django.test import SimpleTestCase

# Create your tests here.
class HomePageTests(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class AboutPageTest(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
```

What else can we test? 

At the moment we are testing the actual URL route for
each page: / for the homepage and /about for the about page.

But remember that we also added a URL name for each page in the 
pages/urls.py file. 


To do that we can use the very handy Django utility function **reverse**. 

Instead of going to a URL path first, it looks for the URL name. 
In general, it is a bad idea to hardcode URLs, especially in templates. 
By using reverse we can avoid this.

For now, we want to test the URL names for our two  pages. 
Import reverse at the top of the file add then add a new unit test for each below.

```python
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomePageTests(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

class AboutPageTest(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
```


Let’s make sure that the correct templates 
-home.html and about.html-
are used on each page 

```python
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class HomePageTests(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

class AboutPageTest(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about.html')
```


and that they display the expected content of

"<h1>Homepage</h1>" and "<h1>About page</h1>" 

respectively.

We can use *assertTemplateUsed* and *assertContains* to achieve this.

```python
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class HomePageTests(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_template_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<h1>Homepage</h1>')
        # self.assertIn(b'<h1>Homepage</h1>', response.content)


class AboutPageTest(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about.html')

    def test_template_content(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, '<h1>About page</h1>')

```

#### Topics
- Request and Response object
- function based vs. class based views
- custom tags and filter
- for loop and if tag
- mixins in views


### Request and Response object

- All views always receive a first argument that contains a request object.
- it has attributes like:
1. request.method
2. request.GET
3. request.POST
4. request.COOKIES
etc.

```python
def homePageView(request):
    print(request)
    print(request.method == 'GET')
    print(request.COOKIES)
   ......
```

- The response object is a file-like object (a I/O stream) and has the usual methods.
- response = **HttpResponse()** # returns response
- **render** also returns response object
- All views must always return 
a response object.

e.g.:

```python
def homePageView(request):
    # print(request)
    # print(request.method == 'GET')
    # print(request.COOKIES)
    context = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'Hello',
        'first': [1, 2, 3],
        'second': [4, 5, 6],
        'today': datetime.now(),
        'notes': "<strong>Note:</strong> Always learn something new!",
        'js_inject':"<script>alert('Hello World')</script>"
    }
    response_render = render(request, 'home2.html', context)
    print('Response:', response_render)
    print('####################################################')
    response = HttpResponse('<h1>Hello</h1>')
    response.write('<div>Hello2</div>')
    response.write('<div>Hello2</div>')
    response.set_cookie('my_cookie', 'my_cookie_value')
    print(response)
    print('####################################################')
    print(HttpResponseForbidden('you are not allowed to enter'))
    print(HttpResponseServerError())
    return response
```

### Function based versus class based

```python
## function based view
def homePageView(request):
    print(request)
```

```python
## class based view
class HomePageView(TemplateView):
    template_name = "home.html"

    def render_to_response(self, context, **kwargs):
        print(self.request.COOKIES.get('my_cookie'))
        if self.request.COOKIES.get('my_cookie') == 'my_cookie_value':
            response = HttpResponse('With cookie')
            return response
        return super().render_to_response(context, **kwargs)
```

## Custom template tags


```bash
├── db.sqlite3
├── django_project_live
├── manage.py
├── pages
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py
│   ├── templatetags
│   │   ├── init.py
│   │   └── my_tags.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── README.md
├── requirements.txt
└── templates
    ├── about.html
    ├── base.html
    ├── header.html
    ├── home2.html
    └── home.html
```

- Template tags are functions.
- Custom template tags must be defined in a directory named templatetags inside an app directory.
- The directory must have an empty __init__.py file.
- The app must be in the INSTALLED_APPS settings constant.
- We can have as many files as we want with any name we want.
- The file with the template tag definition must be loaded in the template, using the load built-in tag.
- The template tag function must be registered in the library.
- It can be done with the simple_tag decorator.


### Simple tag

templates/home2.html 

```html

{% load my_tags %}

<h1>{% hello_world %}</h1>
```

django_project2/pages/templatetags/my_tags.py:

```python
from django import template

register = template.Library()

@register.simple_tag
def hello_world():
    return 'Hello World'
```

- Multiple template tag modules, custom and built-in, can be loaded.
- Custom tags may also accept arguments.
- The inclusion_tag decorator is a shortcut for a template renderer.

### Inclusion_tag

The inclusion_tag is a feature of Django's templating system that lets you define a template tag that renders a specific template. 

### Step 1: Define the `inclusion_tag` to accept an argument

Create `footer_tags.py`:

# pages/templatetags/footer_tags.py

```python
from django import template

register = template.Library()

@register.inclusion_tag('footer.html')
def render_footer(company_name="My Comany"):
    return {'company_name': company_name}
```

### Step 2: Create the template to be included

Create `footer.html`

```html
<!-- templates/footer.html -->
<footer>
    Copyright &copy; {{ company_name }}.
</footer>
```

### Step 3: Use the `inclusion_tag` with an argument in another template

Load the templatetag and use `render_footer` with a specified company name:

```html
{% load footer_tags %}

... rest of your template ...

{% render_footer "AwesomeCo" %}
```

Now, when this template is rendered, the footer will display:

```
Copyright © AwesomeCo.
```

By providing default values in the inclusion tag definition (like "My Company" in our example), you ensure that the tag remains flexible.
It can be used with or without specifying the company name. If no name is provided, it'll default to "My Company".

## Topics

- Mixins
- Django Admin (ORM)

## Using a Mixin in a Django View

Mixins are a way to reuse code across multiple class-based views.
They can be particularly useful when certain patterns of behavior are needed across multiple views.


### 1. Defining the Mixin

First, let's define a mixin that checks if the user's browser accessing the view has a cookie with a special value stored. 

Create `mixin class` :

```python
from django.http import HttpResponseForbidden

class ActiveUserRequiredMixin(object):
    """
    Mixin to ensure the user is active.
    """
    class ActiveRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.COOKIES.get('my_cookie') == 'my_cookie_value':
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseForbidden('You are not allowed to access')
```

### 2. Applying the Mixin to a View

Now that we have our mixin ready, let's apply it to a view. For this example, we'll use a basic `TemplateView`.

```python
from django.views.generic import TemplateView

class DashboardView(ActiveUserRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
```

Note the order of inheritance: the mixin should come before the view base class. This is because the `dispatch` method in the mixin should be the first one to be invoked.

### 3. Configuring the URL

Ensure that the view is reachable by configuring its URL in your `urls.py`.

```python
from django.urls import path
from .views import DashboardView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
```

### 4. Testing the Mixin

1. Run your Django server.
2. Navigate to the `/dashboard/` URL.
3. If there is a cookie with a value my_cookie_value' you would access the dashboard page
4. other you would be directed to `HttpResponseForbidden('You are not allowed to access')`

### 5. Conclusion

Mixins allow you to modularize and reuse specific pieces of functionality across different views. The `ActiveRequiredMixin` is just one simple example. You can build more complex mixins that handle different types of checks, add context data, or even modify the behavior of the view based on specific conditions.
