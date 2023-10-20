# Topic 
- notes for the CreateView
- UpdateView
- DeleteView
- Tests
- ModelForm

# Forms

HTML forms are one of the more complicated and error-prone aspects of web development because any time you accept user input, there are security concerns. 

All forms must be properly rendered, validated, and saved to the database.

Writing this code by hand would be time-consuming and difficult, so Django comes with powerful built-in Forms that abstract away much of the difficulty
for us. 

Django also comes with generic editing views for common tasks like displaying, creating, updating, or deleting a form.


### CreateView

To start, update our base template to display a link to a page for entering new blog posts.

It will take the form <a href="{% url 'post_new' %}"></a> where post_new is the name for our URL.

Your updated file should look as follows: 


```html
<!-- templates/base.html -->
{% load static %}
<html>
<head>
<title>Django blog</title>
<link href="https://fonts.googleapis.com/css?family=\
Source+Sans+Pro:400" rel="stylesheet">

<link href="{% static 'css/base.css’' %}" rel="stylesheet">
</head>
<body>
<div>
<header>
<!-- start new HTML... -->

<div class="nav-left">
    <h1><a href="{% url 'home' %}">Django blog</a></h1>
</div>

<div class="nav-right">
    <a href="{% url 'post_new' %}">+ New Blog Post</a>
</div>

<!-- end new HTML... -->
</header>

{% block content %}

{% endblock content %}
</div>
</body>
</html>
```

- add a new URL for post_new 
- Import BlogCreateView
- add a URL path for post/new/
- give it the URL name post_new to refer to it later in our templates

```python
# blog/urls.py
from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView # new

urlpatterns = [
    path("post/new/", BlogCreateView.as_view(), name="post_new"), # new
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("", BlogListView.as_view(), name="home"),
]
```

- create our view by importing a generic class-based view called CreateView at the top and then subclass it to create a new view called BlogCreateView.

```python
# blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView # new
from .models import Post
class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class BlogCreateView(CreateView): # new
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]

```

Within BlogCreateView, we specify our database model, Post, the name of our template, post_new.html, and explicitly set the database fields we want to expose, which are title, author, and body.

The last step is creating our template, templates/post_new.html:

```html
<!-- templates/post_new.html -->
{% extends "base.html" %}
{% block content %}
    <h1>New post</h1>
    <form action="" method="post">{% csrf_token %}
    {{ form.as_p }}
        <input type="submit" value="Save">
    </form>
{% endblock content %}
```

Let’s break down what we've done:

- on the top line we extended our base template.
- use HTML <form> tags with the POST method since we’re sending data.
- If we were receiving data from a form, for example, in a search box, we would
use GET.
- add a {% csrf_token %} which Django provides to protect our form from cross-site request forgery.
You should use it for all your Django forms.
- then, to output our form data use {{ form.as_p }2}, which renders the specified fields within paragraph <p> tags.
- finally, specify an input type of submit and assign the value “Save”.

### UpdateView

Creating an update form so users can edit blog posts should feel familiar.
We’ll again use a built-in Django class-based generic view, UpdateView, and
create the requisite template, URL, and view.

- add a new link to the post_detail.html so that the option to edit a blog post appears on an individual blog page

```html
<!-- templates/post_detail.html -->

{% extends "base.html" %}

{% block content %}

<div class="post-entry">

<h2>{{ post.title }}</h2>
<p>{{ post.body }}</p>

</div>

<!-- start new HTML... -->

<a href="{% url 'post_edit' post.pk %}">+ Edit Blog Post</a>

<!-- end new HTML... -->

{% endblock content %}
```

We've added a link using <a href>...</a>and the Django template engine’s {% url ... %} tag. Within it, we've specified the target name of our 'URL, which will be called post_edit, and also passed the parameter needed, which is the primary key of the post: post.pk.

create the template file for our edit page called templates/post_edit.html:

```html
<!-- templates/post_edit.html -->

{% extends "base.html" %}

{% block content %}

<h1>Edit post</h1>
<form action="" method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Update">
</form> 
{% endblock content %}
```

- We again use HTML <form></form> tags
- Django’s csrf_token for security
- form.as_p to display our form fields with paragraph tags
- the input tag gives us the the submit button.

Next comes the view.
here we have to subclass our new view BlogUpdateView with UpdateView 

```python
# blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView # new
from .models import Post
class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html" 

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView): # new
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]
```

Notice in BlogUpdateView we assume that the author of the post is not changing;

we only want the title and body text to be editable, hence ["title", "body" ] but not author as is the case for BlogCreateView.

The final step is to update our urls.py file as follows:

```python
# blog/urls.py
from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView, # new
)

urlpatterns = [
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"), # new
    path("", BlogListView.as_view(), name="home"),
] 
```

- At the top, we added our view BlogUpdateView to the list of imported views,
- create a new URL pattern for /post/pk/edit and give it the name post_edit
- Now if you click on a blog entry, you'll see our new + Edit Blog Post hyperlink.

### DeleteView

The process for creating a form to delete blog posts is very similar to that for updating a post. 

We’ll use yet another generic class-based view, DeleteView, create the necessary view, URL, and template.

Let’s start by adding a link to delete blog posts on our individual blog page, post_detail.html.

```html 
<!-- templates/post_detail.html -->
{% extends "base.html" %}
{% block content %}
<div class="post-entry">
    <h2>{{ post.title }}</h2>
    <p>{{ post.body }}</p>
</div>
<div>
<!-- start new HTML... -->
    <p><a href="{% url 'post_edit' post.pk %}">+ Edit Blog Post</a></p>
    <p><a href="{% url 'post_delete' post.pk %}">+ Delete Blog Post</a></p>
<!-- end new HTML... -->
</div>
{% endblock content %}
```

Then create a new file for our delete page template. It will be called templates/post_delete.html and contain the following code:


```html
<!-- templates/post_delete.html -->
{% extends "base.html" %}
{% block content %}
<h1>Delete post</h1>
<form action="" method="post">{% csrf_token %}
    <p>Are you sure you want to delete "{{ post.title }}"?</p>
    <input type="submit" value="Confirm">
</form>
{% endblock content %}
```

Note we are using post.tit1e here to display the title of our blog post. 

We could also just use object.title as it too is provided by DetailView.  

Now update the blog/views.py file by importing DeleteView and reverse_lazy at the top and then create a new view that subclasses DeleteView.

```python
# blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # new
from django.urls import reverse_lazy # new
from .models import Post

    .....
    .....
    .....
    .....

class BlogDeleteView(DeleteView): # new
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
```

- The DeleteView specifies a model which is Post
- a template which is post_delete.html
- a third field called success_url

after a blog post is deleted, we want to redirect the user to another page which is, in our case, the homepage at home.
we are using reverse_lazy here and not reverse. 

Both reverse and reverse_lazy perform the same
task: generating a URL based on an input like the URL name. 

The difference is when they are evaluated. reverse executes right away,
so when BlogDeleteView is executed, immediately the model, template_name,and success_url methods are loaded. 

But the success_url needs to find out what the resulting URL path is associated with the URL name “home.” 

It can’t always do that in time. 

That’s why we use reverse_lazy in this
example:

it delays the actual call to the URLConf until the moment it is needed, not when our class BlogDeleteView is being evaluated.

The moment BlogDeleteView is called, reverse needs to have the information from the URLconf about what the proper route is for the URL name “home.”

But it might not have that information in time for the success_url.

***https://docs.djangoproject.com/en/4.2/ref/urlresolvers/#reverse-lazy**


CreateView and UpdateView also have redirects. 

Yet, we did not have to specify a success_ur1l because Django
will automatically use **get_absolute_url()** on the model object if available. 

And the only way to know about this trait is to read and remember the
docs, which talk about model forms and success_url. 

- create a URL by importing our view BlogDeleteView and adding a new pattern:

```python
# blog/urls.py
from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView, # new
)
urlpatterns = [
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(),
        name="post_edit"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(),
        name="post_delete"), # new
    path("", BlogListView.as_view(), name="home"),
]
```

### Tests

Time for tests to make sure everything works now-and in the future-as expected.

We've added new views for create, update, and delete, so that means three new tests:

- def test_post_createview
- def test_post_updateview
- def test_post_deleteview

Update your existing tests.py file with new tests below test_post_detailview as follows.







