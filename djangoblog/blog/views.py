from django.shortcuts import render
from .models import Article
# Create your views here.

def hello_world(request):
    return render(request, 'blog/hello_world.html')

def index(request):
    articles = Article.objects.all()
    article = articles[0]
    return render(request, 'blog/index.html', context={
        'article': article,
    })

def detail(request):
    articles = Article.objects.all()
    article = articles[0]
    return render(request, 'blog/detail.html', context={
        'article': article,
    })