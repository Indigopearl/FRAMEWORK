## Topic 

1. Testing (done)
2. create a new project ('blog' project)
3. recap static, ListView, css
4. DetailView
5. Primary Key and Foreign Key in django models 
6. User Table
7. Parameterized urls / routes

# Blog App

we will build a Blog application that allows users to create, edit, and delete posts. 
The homepage will list all blog posts, and each blog post
will have a dedicated page.

We'll also use CSS for styling.



### Initial Set Up

 make a new directory for our code called blog
- install Django in a new virtual environment called .venv
- create a new Django project called django_project
- create a new appblog
- perform a migration to set up the database
- update django_project/settings.py

Let’s implement them now in a new command line terminal. Start with the new directory, a new virtual environment, and activate it.

```bash
$ mkdir blog

$ cd blog

$ python3 -m venv .venv

$ source .venv/bin/activate
$ (.venv)

(.venv) $ python -m pip install django

(.venv) § django-admin startproject django_project .
(.venv) $ python manage.py startapp blog
(.venv) $ python manage.py migrate
```

Add the blog App to the project.


### Recap Databases

A database is a place to store and access different types of data, and there are two main types of databases:
relational and non-relational.

*A relational database* stores information in tables containing columns and rows, roughly analogous to an Excel spreadsheet. 
The columns define what information can be stored; the rows contain the actual data. 
Frequently, data in separate tables have some relation to each other, hence the term “relational
database” to describe databases with this structure of tables, columns, and rows.

*A non-relational database* is any database that doesn’t use the tables, fields, rows, and columns inherent in relational databases to structure its data:
examples include document-oriented, key-value, graph, and wide-column.

Relational databases are best when data is consistent, structured, and relationships between entities are essential. 

Non-relational databases have advantages when data is not structured, needs to be flexible in size or shape, and must be open to change in the future. 


### Django’s ORM

An ORM (Object-Relational Mapper) is a powerful programming technique that makes working with data and relational databases much easier. 

In the case of Django, its ORM means we can write Python code to define database models; we don’t have to write raw SQL ourselves. 
And we don't have to worry about subtle differences in how each database interprets SQL. 

Instead, the Django ORM supports five relational databases: 
SQLite, PostgreSQL, MySQL, MariaDB, and Oracle. 

It also comes with support for migrations which provides a way to track and sync database changes over time. 

In sum, the Django ORM saves developers a tremendous amount of time and is one of the major reasons why Django is so efficient.

While the ORM abstracts much of the work, we still need a basic understanding of relational databases if we want to implement them correctly. 

let’s look at structuring the data in our Blog database.

Recall that we create a table by adding a column to define a “field” of data. 

So, for example, we could start with a table called “Post” with columns for the 
1. title, 
2. author, and 
3. body text. 

If we drew this out as a simple schema, it would look something like this:

```shell
Post Schema
Post
TITLE AUTHOR BODY
```

And the actual database table with columns and rows would look like this:

#### Post Database Table

```shell
TITLE           AUTHOR  BODY
Hello, World!   WSV     My first blog post. Woohoo!
Goals Today     WSV     Learn Django and build a blog application.
3rd Post        WSV     This is my 3rd entry.
```

### Post Database Table

At the beginning, we used the command python manage.py startapp blog to create a new blog app within our project,
resulting in a blog directory containing several additional files, including **blog/models.py**. 

In Django, a models.py file is the single, definitive source of
information about your data, and it contains the necessary fields and behaviors of the data being stored. 

To mimic the previous Post table using the Django ORM, add the following code to the blog/models.py file.

```python
# blog/models.py
from django.db import models
class Post(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()

    def _ str_ (self):
        return self.title
```

At the top of the file, we import models. 

Next, we create a subclass of models.Model called Post, which provides access to everything within django.db.models.Model. 
And from there, we have added three additional fields (think of them as columns) for title, author, and body. Each field must have an appropriate field type. 

The first two use CharField with a maximum character length of 200, while the third uses TextField, which is intended for a large amount of text.

Adding the __str__method is technically optional, it is a best practice to ensure a human-readable version of our model object in the Django admin. 

In this case, it will display the title field of any blog post.

Now that our new database model exists, we need to create a new migration record for it and migrate the change so it is applied to our database. 

Stop the server with Control+c. You can complete this two-step process with the commands below:

```shell
(.venv) $ python manage.py makemigrations blog
(.venv) $ python manage.py migrate
```

The database is now configured, and there is a new migrations directory within the blog app directory containing our changes.

### Primary Keys and Foreign Keys

1. Primary Key

Because relational databases have relationships between tables, there needs to be an easy way for them to communicate. 

The solution is adding a column- known as a primary key that contains unique values. 

When there is a relationship between two tables, the primary key is the link maintaining a consistent
relationship. 

Primary keys are a standard part of relational database design.

As a result, Django automatically adds an auto-incrementing primary key to our database models.

Its value starts at 1 and increases sequentially to 2, 3, and so on. 

The naming convention is <table_id>, meaning that for a model called Post the primary key column is named post_id.


2. Foreign Key

Now that we know about primary keys, it’s time to see how they are used to link tables. 

When you have more than one table, each will contain a column of primary keys starting with 1 and increasing sequentially, just like in our Post model example. 

In our blog model, consider that we have a field for author, 3 but in the actual Blog app, we want users to be able to log in and create blog posts. 

That means we’ll need a second table for users to link to our existing table for blog posts. 

Fortunately, authentication is such a common - and challenging to implement well - feature on websites that Django has an entire built-in  authentication system that we can use. 

We can use it to add signup, login, logout, password reset, and other functionality. 

But for now, we can use the Django auth user model, which comes with various fields. 


How do we link these two tables together so they have a relationship? 

We want the author field in Post to link to the User model so that each post has an author that corresponds to a user. 

And we can do this by linking the User model primary key, user_id, to the Post.author field. 
A link like this is known as a foreign key relationship. 

Here is how it looks in the code. We only need to change the author field in our Post model.

```python
# blog/models.py
from django.db import models
from django.urls import reverse
class Post(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE,) # new
    body = models.TextField()

    def _ str_ (self):
        return self.title

```

The ForeignKey field defaults to a many-to-one relationship, meaning one user can be the author of many different blog posts but not the other way around.

It is worth mentioning that there are three types of foreign relationships:
1. many-to-one,
2. many-to-many, and 
3. one-to-one. 

A many-to-one relationship, as we have in our Post model, is the most common occurrence. 

A many-to-many relationship would exist if there were a database tracking authors and books:
each author can write multiple books, and each book can have multiple authors. 

A one-to-one relationship would exist in a database tracking people and
passports: only one person can have one passport.

Note that when an object referenced by a ForeignKey is deleted, an additional on_delete argument must be set. 

Since we have updated our database models again, we should create a new migrations file and then migrate the database to apply it.

```Shell
(.venv) $ python manage.py makemigrations blog
(.venv) $ python manage.py migrate
```

A second migrations file will now appear in the blog/migrations directory that documents this change.
The newly created migration file reflects the changes we made to our model. (changed from charField to ForeignKey)

### Admin

We need a way to access our data. 
Enter the Django admin! First, create a superuser account by typing the command below and following the prompts to set up an email and password. 

Note that typing your password it will not appear on the screen for security reasons.

```Shell
(.venv) $ python manage.py createsuperuser
Username : piet
Email:
Password:
Password (again):
Superuser created successfully.
```

Register model in your admin:

```python
# blog/admin.py

from django.contrib import admin
from .models import Post

admin.site.register(Post)
```
Now that our database model is complete, we must create the necessary views, URLs, and templates to display the information on our web application.

We want to display our blog posts on the homepage, so well first configure our app-level blog/urls.py file and then our project-level
django_project/urls.py file to achieve this.

```python
# blog/urls.py
from django.urls import path
from .views import BlogListView

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
]
```

While it’s optional to add a named URL, it’s a best practice you should adopt as it helps keep things organized as your number of URLs grows.

We also should update our django_project/urls.py file so that it knows to forward all requests directly to the blog app.

```python
# django_project/urls.py
from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")), # new
]
```
We've added include on the second line and a URL pattern using an empty string , " ", indicating that URL requests should be redirected as is to blog’s URLs for further instructions.

### Views

In our views file, add the code below to display the contents of our Post model using ListView. 

It is quite rare that we use the default views.py code of
**from django.shortcuts import render** code that Django provides.

```python
# blog/views.py
from django.views.generic import ListView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = "home.html"

```

On the top two lines, we import ListView and our database model Post. 
Then we subclass ListView and add links to our model and template, saving us
a lot of code versus implementing it all from scratch.

### Templates

we’ll start with a base.htm1 file and a home.htm1 file that inherits from it. 

Then later, when we add templates for creating and editing blog posts, they too can inherit from base.html.

```shell
(.venv) $ mkdir templates
```

Create two new templates in your text editor: templates/base.html and templates/home.html. 


Then update django_project/settings.py so Django knows to look there for our templates.

```python
# django_project/settings.py
TEMPLATES = [
    {   
        "DIRS": [BASE_DIR / "templates"], # new
    },
]
```

And create the base.html template as follows.

```html
<!-- templates/base.html -->
<html>
<head>
<title>Django blog</title>
</head>
<body>
<header>
<h1><a href="{% url 'home' %}">Django blog</a></h1>
</header>
<div>
{% block content %}
{% endblock content %}

</div>
</body>
</html>
```

Note that code between {% block content %} and {% endblock content %} can be filled by other templates. Speaking of which, here is the code
for home.html.

```html
<!-- templates/home.html -->
{% extends "base.html" %}
{% block content %}
{% for post in post_list %}
<div class="post-entry">

<h2><a href="">{{ post.title }}</a></h2>

<p>{{ post.body }}</p>
</div>
{% endfor %}
{% endblock content %}
```
At the top, we note that this template extends base.html and then wraps our desired code with content blocks. 

We use the Django Templating Language to set up a simple for loop for each blog post. 

Note that post_1ist comes from ListView and contains all the objects in our view of the model post.


### Static Files

We need to add some CSS to our project to improve the styling.

CSS, JavaScript, and images are a core piece of any modern web application and within
the Django world, are referred to as “static files.”

By default, Django will look within each app for a folder called “static”; in other words, a folder called blog/static/. 
If you recall, this is similar to how templates are treated.

As Django projects grow in complexity over time and have multiple apps, it is often simpler to reason about static files if they are stored in a single, project-
level directory instead. 

That is the approach we will take here.

```shell
(.venv) $ mkdir static
```
Then we must tell Django to look for this new folder when loading static files. 

If you look at the bottom of the django_project/settings.py file,
there is already a single line of configuration:

```python
# django_project/settings.py
STATIC_URL = "static/"
```

We have to add: 

```python
# django_project/settings.py
STATICFILES_DIRS = [BASE_DIR / "static"] # new
```
STATIC_URL is the URL location of static files in our project, aka at static/.

STATICFILES_DIRS defines additional locations the built-in staticfiles app will traverse looking for static files beyond an app/static folder.

We need to set it to have a project-level static folder instead, and it is also necessary for local static file viewing. 


Next, create a css directory within static.

create a new file within this directory called static/css/base.css.

```css
/* static/css/base.css */
body {
font-family: 'Source Sans Pro', sans-serif;
font-size: 18px;
}

header {
border-bottom: 1px solid #999;
margin-bottom: 2rem;
display: flex;
}

header h1 a {
color: red;
text-decoration: none;
}
.nav-left {
margin-right: auto;
}
.nav-right {
display: flex;
padding-top: 2rem;
}
.post-entry {
margin-bottom: 2rem;
}
.post-entry h2 {
margin: 0.5rem 0;
}
.post-entry h2 a,
.post-entry h2 a:visited {
color: blue;
text-decoration: none;
}

.post-entry p {
margin: 0;
font-weight: 400;
}

.post-entry h2 a:hover {
color: red;
}

```

We need to add the static files to our templates by adding {% load static %} to the top of base.html.

Because our other templates inherit from base.htm1, we only have to add this once. 

refactored base.html:

```html
<!-- templates/base.html -->
<html>
<head>
<title>Django blog</title>
{% load static %}  
<link rel="stylesheet" href="{% static 'css/base.css' %}">
</head>
```

add a custom font:

```html
<!-- templates/base.html -->
{% load static %}
<html>
<head>
<title>Django blog</title>
<link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400"
rel="stylesheet">
<link href="{% static 'css/base.css' %}" rel="stylesheet">
</head>

```

### Individual Blog Pages

Start with the view. We can use the generic class-based DetailView to simplify things. 
At the top of the file, add DetailView to the list of imports and then create a new view called BlogDetailView.

```python
# blog/views.py
from django.views.generic import ListView, DetailView # new
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView): # new
    model = Post
    template_name = "post_detail.html"
```

- we define the model we're using, Post
- we define the template we want it associated with, post_detail.html.

Create a new template file for a post detail called templates/post_detail.html:

```html
<!-- templates/post_detail.html -->
{% extends "base.html" %}
{% block content %} 
<div class="post-entry"> 
    <h2>{{ post.title }}</h2>
    <p>{{ post.body }}</p>
</div> 
{% endblock content %} 
```

- this template inherits from base.html.
- display the title and body from our context object (here it is post; DetailView makes accessible as post.) 

Add a new URL path for our view, which we can do as follows.

```python
# blog/urls.py
from django.urls import path
from .views import BlogListView, BlogDetailView # new
urlpatterns = [
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"), # new
    path("", BlogListView.as_view(), name="home"),
]
```
All blog post entries will start with post/.

To represent each post entry, we can use the auto-incrementing primary key, which is represented as an integer, <int:pk>. 

The pk for our first “Hello, World” post is 1; for the second post, it is 2; and so on. 

Therefore, when we go to the individual entry page for our
first post, we can expect that its URL pattern will be post/1/.

To make our life easier, we should update the link on the homepage so we can directly access individual blog posts from there. Swap out the current empty
link,<a href=""> for<a href="{% url 'post_detail' post.pk %}">.

But before add the get_absolute_url method to the Post model:

```python
from django.db import models
from django.urls import reverse

class Post(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"pk": self.pk}) 
```


### get_absolute_url()

we defined a get_absolute_url()
method in our model that defined a canonical (meaning official) URL for the model.

So we can take the simpler step of using 
<a href="{{ post.get_absolute_url }}">{{ post.title }}</a></h2>in the template instead.

```html
<!-- templates/home.html -->
{% extends "base.html" %}
{% block content %}
{% for post in post_list %}
<div class="post-entry">
<h2><a href="{{ post.get_absolute_url }}">{{ post.title }}</a></h2> </-- new -->
<p>{{ post.body }}</p>
</div>
{% endfor %}
{% endblock content %}
```

URL paths can and do change over the lifetime of a project.

With the previous method, if we changed the post detail view and URL path, we’d have to go
through all our HTML and templates to update the code, a very error-prone and hard-to-maintain process.

By using get_absolute_url () instead, we
have one single place, the models.py file, where the canonical URL is set, so our templates don’t have to change.


### Topic

- adding style to out project (static)
- refactor and add a base.html file
- add notes
- add tests (detail page)
- add Forms (creating, editing, deleting)

### Tests

Our Blog project has added new functionality we have not seen or tested before. 

The Post model has multiple fields, we have a user for the first
time, and there is a list view of all blog posts and a detailed view for each blog post. 

To begin, we can set up our test data and check the Post model’s content:

```python
# blog/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )

        cls.post = Post.objects.create(
                title="A good title",
                body="Nice body content",
                author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "A good title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")
```

At the top, we import **get_user_model()** to refer to our User and then added TestCase and the Post model. 

Our class BlogTests contains set-up data for both a test user and a test post. 

Currently, all the tests are focused on the Post model, so we name our test test_post_model. 

It checks that all three model fields return the expected values. 

Our model also has new tests for the __str__and get_absolute_url methods.

Previously, we implemented tests to check that:
- expected URLs exist and return a 200 status code
- URL names work and return a 200 status code
- the correct template name is used
- the correct template content is outputted

lets add them as well:

```python
# blog/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )

        cls.post = Post.objects.create(
                title="A good title",
                body="Nice body content",
                author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "A good title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")

    def test_url_exists_at_correct_location_listview(self): # new
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self): # new
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self): # new
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nice body content")
        self.assertTemplateUsed(response, "home.html")

    def test_post_detailview(self): # new
        response = self.client.get(reverse("post_detail",
                    kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)    
```

For test_post_detailview, we have to pass in the pk of our test post to the response. 

we don’t want a response at the URL /post/100000/ because we have not created that many posts yet! 

It is always good to sprinkle in examples of incorrect tests that should pass through failure using the no_response method to ensure your tests aren’t all blindly passing for some reason.

A common gotcha when testing URLs is failing to include the preceding slash /. 

### Git 

Now is a good time to commit.

```shell
(.venv) §$ git init
```

Don't forget to ignore the virtual .pyc and database files.

```shell
.venv/
db.sqlite3
*.pyc
```

Then add and commit the newly created and changed files:

```shell
(.venv) $ git add .
(.venv) $ git add commit -m "tests added"
```


