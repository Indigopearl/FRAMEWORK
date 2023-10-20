from django.views.generic.edit import CreateView
from .models import Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ["title", "content"]
    template_name = "article_form.html"
