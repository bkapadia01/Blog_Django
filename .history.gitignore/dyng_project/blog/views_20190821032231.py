from django.shortcuts import render
from django.http import HttpResponse

post = [
    {
        'author': 'bkap',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'August 27, 2019'
    },
        {
        'author': 'john doe',
        'title': 'blog post 2',
        'content': 'second post content',
        'date_posted': 'August 24, 2019'
    }
]

def home(request):
    context = {
        'posts': post
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
# Create your views here
