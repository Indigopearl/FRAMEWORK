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