from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Article
# Create your views here.

def hello_world(request):
    return render(request, 'blog/hello_world.html')

def index(request):
    articles = Article.objects.all()
    per_page = request.GET.get('per_page', 5)
    current_page = request.GET.get('current_page', 1)
    p = Paginator(articles, per_page)
    total_page = p.num_pages
    articles = p.get_page(current_page)
    top5_articles = Article.objects.all().order_by('-publish_date')[:5]
    return render(request, 'blog/index.html', context={
        'articles': articles,
        'total_page': total_page,
        'per_page': per_page,
        'current_page': current_page,
        'top5_articles': top5_articles,
    })

def detail(request, id):
    articles = Article.objects.all()
    current_article = None
    previous_index = 0
    next_index = 0
    previous_article = None
    next_article = None
    for index, article in enumerate(articles):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(articles) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if article.id == id:
            current_article = article
            previous_article = articles[previous_index]
            next_article = articles[next_index]
            break
    content_list = current_article.content.split('\n')
    return render(request, 'blog/detail.html', context={
        'articles': articles,
        'current_article': current_article,
        'content_list': content_list,
        'id': id,
        'previous_article': previous_article,
        'next_article': next_article,
    })