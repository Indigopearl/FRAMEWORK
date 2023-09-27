from django.shortcuts import render
from django.http import HttpResponse
from .data import POSTS


def blog_posts(request):
    # Convert the list of blog posts to plain text
    plain_text_posts = "\n\n".join(
        [f"Title: {post['title']}\nContent: {post['content']}" for post in POSTS]
    )
    return HttpResponse(plain_text_posts, content_type="text/plain")
