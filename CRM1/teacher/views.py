from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('hello world')

def test1(request, id):
    return HttpResponse('%s号老师' % id)

def test2(request, id):
    return HttpResponse('%s号老师' % id)

def test3(request, id, name):
    return HttpResponse('%s号老师：%s' % (id, name))

def login(requset):
    now = datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')
    now1 = datetime.now()
    return render(requset, 'teacher/login.html', context={
        'now': now,
        'now1': now1,
    })

def index(request):
    return render(request, 'teacher/index.html')