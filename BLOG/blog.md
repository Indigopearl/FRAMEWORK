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

Note that when an object referenced by a ForeignKey is deleted, an additional on_delete argument must be set. 

Since we have updated our database models again, we should create a new migrations file and then migrate the database to apply it.

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