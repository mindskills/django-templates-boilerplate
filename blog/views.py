from django.shortcuts import render

from blog.models import Post


def some_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/main.html', context={'posts': posts})
