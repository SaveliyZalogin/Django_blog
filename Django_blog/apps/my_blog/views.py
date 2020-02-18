from django.shortcuts import render
from django.http import HttpResponse
import random
from Django_blog.apps.my_blog.models import Post
from Django_blog.apps.my_blog.models import Key_word


def hello():
    form = '<button>Test me for me pls!?!</button>'
    return form


def btn():
    i = 1
    f = 1
    b = ''
    for i in range(1, 10):
        b += '{}'.format(str(i) + '*' + str(f) + '=' + str(i * f))
        i += 1
    return b


def index(request):
    post_list = Post.objects.all()
    key_word = Post.objects.all()
    context = {
        'posts': post_list,
        'key_word': key_word,
    }
    return render(request, "index.html", context)


def about(request):
    context = {


    }
    return render(request, "about.html", context)


def contacts(request):
    context = {


    }
    return render(request, "contacts.html", context)


def post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'title': Post.post_title,
        'text': Post.post_text,
        'post': post,
    }
    return render(request, "posts.html", context)
