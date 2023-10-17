# Message Board App

- admin interface
- orm
- testing

## Setup

```bash
$ mkdir message-board

$ cd message-board

$ python3 -m venv .venv

$ source .venv/bin/activate
$ (.venv)

(.venv) $ python -m pip install django

(.venv) § django-admin startproject django_project .
(.venv) $ python manage.py startapp posts
```

```shell
(.venv) $ python manage.py migrate
```

```shell
.
├── db.sqlite3
├── django_project
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── posts
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
```


Activating Post Model:

*python manage.py makemigrations posts* 
*python manage.py migrate*


*python manage.py createsuperuser*