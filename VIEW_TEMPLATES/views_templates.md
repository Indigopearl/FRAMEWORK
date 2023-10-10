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