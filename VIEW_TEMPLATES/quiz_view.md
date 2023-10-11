
## 3
```
{{ value|add:"2" }}
```

if value is 4, then the output will be 6.

This filter will first try to coerce both values to integers. If this fails, it’ll attempt to add the values together anyway. This will work on some data types (strings, list, etc.) and fail on others. If it fails, the result will be an empty string.

For example, if we have:

```
{{ first|add:second }}
```
and first is [1, 2, 3] and second is [4, 5, 6], then the output will be [1, 2, 3, 4, 5, 6].


```
{{ value|lower }}
```
If value is Totally LOVING this Album!, the output will be totally loving this album!.


```
{{ value|date:"D d M Y" }}
```
If value is a datetime object (e.g., the result of datetime.datetime.now()), the output will be the string 'Wed 09 Jan 2008'.


## 6
```html
#header.html
<header style="border: 2px solid red;">
    <h1>Welcome to My Site</h1>
    <nav>
      <a href="{% url 'home' %}">Home</a> | <a href="{% url 'about' %}">About</a>
    </nav>
</header>

#base.html
{% include "header.html" %}

{% block content %} {% endblock content %}

```

```

```

```

```
