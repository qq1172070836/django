from django.shortcuts import render

# Create your views here.

def hello_world(request):
    return render(request, 'blog/hello_world.html')

def index(request):
    return render(request, 'blog/index.html')