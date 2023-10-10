## What is a Web Framework?

- serves as a template with predefined functionalities
- increases development of web apps

- it's like a swiss army knife 
- aids the development of web applications and web APIs
- provides libraries for database access, templating, session management, and more


## Key Features of Django:

**Batteries-Included Philosophy**:
This means it provides everything developers need to build a web application from start to finish, without needing to rely on external libraries for core functionality.

**ORM (Object-Relational Mapping)**:
- it that abstracts the process of working with databases

Instead of writing raw SQL queries, developers define the structure of the database using Python classes, and Django handles the rest.

**Automatic Admin Interface**:
- One of Django's most powerful features
- Given the structure of your database, Django can automatically generate a sophisticated admin interface

**Security**:
- Django provides built-in protection against many common web attacks, such as Cross Site Scripting (XSS), Cross Site Request Forgery (CSRF), and SQL Injection.

**Migration System**:
- Allows developers to change the structure of the database over time without having to recreate it from scratch

**Extensibility**: 
- Django is designed to be highly extensible.
- It has a robust system of 'apps' that can be plugged into a project.
- This modular approach lets developers reuse components across multiple projects.

**Middleware Support**:
Middleware classes allow for processing of request and response globally before they reach the view or after they leave the view.


## Why Use Django?

**Rapid Development**: 
Thanks to the tools and libraries Django provides out-of-the-box, developers can create applications rapidly without needing to reinvent the wheel.

**Highly Scalable**: 
Some of the biggest websites, like Instagram, have been built using Django.
This proves its capability to scale and handle large amounts of traffic.

**Huge Community**:
Being one of the most popular web frameworks means a huge community of developers. This translates to numerous plugins, tutorials, and support.

**Mature and Robust**: Launched in 2005, Django has proven itself as a mature and robust framework suitable for a wide range of applications, from simple websites to complex web platforms.


# Setup

1. Create Virtual environment:
```bash
python3.8 -m venv .venv
```
**You should use a dedicated virtual environment for each Python project.**

```bash
source .venv/bin/activate
```

2. Initialize git repository
3. Ignore your virtual environment:

add `/.venv/` to `.gitignore` file.

4. Install Django

`python3.8 -m pip install django`

# Creating a project

`django-admin startproject django_project .`

that command will create the following folder structure:

├── django_project
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

**starting project:**

`python manage.py runserver`

**`manage.py`**:
- A command-line utility that allows you to interact with your project in various ways such as running the development server, running tests, creating migrations, etc.
- executes various Django commands
- You'll often use it with commands like `python manage.py runserver` to start the development server.

**`__init__.py`**:
- An empty file that tells Python that this directory should be treated as a package or module.

**`asgi.py`**:
- Stands for Asynchronous Server Gateway Interface.
- A newer standard for asynchronous web servers and apps

**`settings.py`**:
- Contains settings for your Django project.
- This is where you'll define database configurations, static and media files handling, installed apps, middleware, templates settings, etc.

**`urls.py`**:
- Contains the URL declarations for the Django project.
- It's essentially a table of contents for your app, where you define URL patterns and associate them with view functions or classes.
- Think of it as a map or router for incoming web requests.

**`wsgi.py`**:
- Stands for Web Server Gateway Interface.
- An interface between web servers and web applications.

# Create An App

- djang uses the concept of projects and apps to keep the code clean and readable
- a singe top-level Django project can contain multiple apps
- each app controls an isolated piece of functionality
- each app should have a clear function

to create an app run:

`python manage.py startapp pages`

this will generate the following folder structure:

pages
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py

# Adding the App to our project:

1. add `pages.apps.PagesConfig` to INSTALLED_APPS in settings.py

2. create a view function in `pages/views.py`

3. create a file named urls.py in the pages directory

4. add the pages url to `django_project/urls.py`

# Requirements.txt

We want  a record of packages installed in our virtual environment.
The current bes practice is to create a requirement.txt file with this information.

`pip freeze > requirments.txt`

# Loading the requirements

When other devs clone your repo, the can use the requirements.txt to install all packages:

`source .venv_from_dev/bin/active`

`pip install -r requirements.txt`






