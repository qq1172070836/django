from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Student, StudentDetail, Grade, Course, Enroll

# Create your views here.

def base(request):
    return render(request, 'student/base.html')

def login(request):
    if request.method == 'POST':
        if request.POST.get('user') == 'lin' and request.POST.get('password') == 'lin':
            request.session['name'] = request.POST.get('user')
            request.session.set_expiry(60) # 设置过期时间
            return redirect('student:student_list')
    return render(request, 'student/login.html')

def logout(request):
    request.session.flush()
    return redirect('student:student_list')

def student_list(request):
    section = '学生列表'
    name = request.session.get('name', '游客')
    search = request.GET.get('search', '').strip()
    if search:
        if search.isdigit():
            stus = Student.objects.filter(Q(is_delete=0) & Q(qq=search) | Q(phone=search))
        else:
            stus = Student.objects.filter(is_delete=0, name=search)
    else:
        stus = Student.objects.filter(is_delete=0)
    stus = stus.order_by('-c_time')
    # 分页功能
    # 总数据total_num
    total_num = stus.count()
    # 页长per_page
    per_page = request.GET.get('per_page', 10)
    # 当前页current_page
    current_page = request.GET.get('current_page', 1)
    p = Paginator(stus, per_page)
    stus = p.get_page(current_page)
    total_page = p.num_pages

    return render(request, 'student/student_list.html', context={
        'section': section,
        'name': name,
        'stus': stus,
        'search': search,
        'per_page': per_page,
        'current_page': current_page,
        'total_page': total_page,
    })

def student_detail(request, pk):
    section = '学生详情'
    stu = Student.objects.get(pk=pk)
    grades = Grade.objects.all()
    return render(request, 'student/student_detail.html', context={
        'section': section,
        'stu': stu,
        'grades': grades,
    })

def student_add(request):
    section = '添加学生'
    grades = Grade.objects.all()
    if request.method == 'GET':
        return render(request, 'student/student_detail.html', context={
            'section': section,
            'grades': grades,
        })
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'age': request.POST.get('age'),
            'sex': request.POST.get('sex'),
            'qq': request.POST.get('qq'),
            'phone': request.POST.get('phone'),
            'grade_id': request.POST.get('grade_id'),
        }
        stu = Student.objects.create(**data)
        # print(stu)
        StudentDetail.objects.create(
            college=request.POST.get('college'),
            student=stu,
        )
        return redirect('student:student_list')

def student_del(request, pk):
    stu = Student.objects.get(pk=pk)
    stu.is_delete = 1
    stu.save()
    return redirect('student:student_list')

def student_edit(request, pk):
    section = '编辑学生'
    grades = Grade.objects.all()
    stu = Student.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'student/student_detail.html', context={
            'section': section,
            'grades': grades,
            'stu': stu,
        })
    if request.method == 'POST':
        grade_id = request.POST.get('grade_id')
        grade = Grade.objects.get(pk=grade_id)
        stu.name = request.POST.get('name')
        stu.age = request.POST.get('age')
        stu.sex = request.POST.get('sex')
        stu.qq = request.POST.get('qq')
        stu.phone = request.POST.get('phone')
        stu.grade = grade
        stu.studentdetail.college = request.POST.get('college')
        stu.studentdetail.student = stu
        stu.save()
        return redirect('student:student_list')