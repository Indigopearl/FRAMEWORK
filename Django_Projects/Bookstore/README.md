```
1.InitializeaDjangoprojectcalled`bookstore`
```

```
2.Createanappcalled`books`forthebookstoreproject.
```

```
3.Addthe`books`apptothe`INSTALLED_APPS`inthe`settings.py`fileoftheproject.
```

```
4.Addthefollowingcodetothe`books/models.py`file:
```

```
    ```python
```

```
    class Author(models.Model):
```

```
        first_name = models.CharField(max_length=100)
```

```
        last_name = models.CharField(max_length=100)
```

```
        address = models.CharField(max_length=200, null=True)
```

```
        zip_code = models.IntegerField(null=True)
```

```
        telephone = models.CharField(max_length=100, null=True)
```

```
        join_date = models.DateField()
```

```
        popularity_score = models.IntegerField()
```

```

```

```
    class Books(models.Model):
```

```
        title = models.CharField(max_length=100)
```

```
        price = models.IntegerField(null=True)
```

```
        published_date = models.DateField()
```

```

```

```
    class Publisher(models.Model):
```

```
        publisher_name = models.CharField(max_length=200)
```

```
        join_date = models.DateField()
```

```
        popularity_score = models.IntegerField()
```

```

```

```
    class User(models.Model):
```

```
        username = models.CharField(max_length=100)
```

```
        first_name = models.CharField(max_length=100)
```

```
        last_name = models.CharField(max_length=100)
```

```
        address = models.CharField(max_length=200, null=True)
```

```
        email = models.CharField(max_length=100)
```

```
        telephone = models.CharField(max_length=100, null=True)
```

```

```

```
    class Genre(models.Model):
```

```
        name = models.CharField(max_length=150)
```

```
    ```
```

```

```

```
5.Createa`followers`fieldinthe`Author`modelthatisaManytoManyRelationshipwith`User`
```

```
6.Createa`author`fieldinthe`Books`modelthatisaOnetoManyRelationshipwith`Author`
```

```
7.Createa`publisher`fieldinthe`Books`modelthatisaOnetoManyRelationshipwith`Publisher`
```

```
8.Createa`genre`fieldinthe`Books`modelthatisaOnetoManyRelationshipwith`Genre`
```

```
9.Createanabstractmodelforthe`User`and`Author`classestoinheritfrom.
```

```
10.Changetheorderingbehaviourofthe`Books`modeltouse`published_date`(descending)and`price`(ascending)
```
