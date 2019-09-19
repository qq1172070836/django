from datetime import datetime
import os

from django.shortcuts import render
from django.http import HttpResponse

from CRM.settings import MEDIA_ROOT

# Create your views here.

def hello(request):
    return HttpResponse('hello world')

def index(request):
    get_user = request.GET.get('user')
    get_password = request.GET.get('password')
    post_user = request.POST.get('user')
    post_password = request.POST.get('password')

    if request.method == "POST":
        file = request.FILES.get('file')
        print(file, type(file), dir(file))
        filename = file.name
        # 当天文件保存到当天文件夹
        day_dir = datetime.now().strftime('%Y%m%d')
        dir_path = os.path.join(MEDIA_ROOT, day_dir)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        file_dir = os.path.join(dir_path, filename)
        with open(file_dir, 'wb') as f:
            for line in file.chunks():
                f.write(line)

    num = request.COOKIES.get('num')
    if num:
        num = int(num) + 1
    else:
        num = 1

    response =  render(request, 'teacher/index.html', context={
        'get_user': get_user,
        'get_password': get_password,
        'post_user': post_user,
        'post_password': post_password,
        'num': num,
    })
    response.set_cookie('num', num)
    return response