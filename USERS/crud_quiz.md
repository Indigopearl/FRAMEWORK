### get objects by primary key 
from blog.models import Post
from django.contrib.auth.models import User


Post.objects.get(pk=1)


Post.objects.filter(author=User.objects.get(pk=1).id)

>>> new_post = Post(title='Bla', author=User.objects.get(pk=1),body='lorem again')
>>> new_post.save()



post request:

request.POST.get('email')