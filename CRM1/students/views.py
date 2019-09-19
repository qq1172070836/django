import os
from datetime import datetime

from django.shortcuts import render

from CRM1.settings import MEDIA_ROOT
from .models import Student

# Create your views here.

def login(request):
    get_user = request.GET.get('user')
    get_password = request.GET.get('password')
    post_user = request.POST.get('user')
    post_password = request.POST.get('password')

    if request.method == 'POST':
        file = request.FILES.get('file')
        filename = file.name
        # 当天上传的文件放到当天文件夹
        date_dir = datetime.now().strftime('%Y%m%d')
        dir_path = os.path.join(MEDIA_ROOT, date_dir)
        print(dir_path)
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

    response = render(request, 'students/login.html', context={
        'get_user': get_user,
        'get_password': get_password,
        'post_user': post_user,
        'post_password': post_password,
        'num': num,
    })
    response.set_cookie('num', num)
    return response

def student_list(request):
    stus = Student.objects.all()
    return render(request, 'students/student_list.html', {
        'stus': stus,
    })