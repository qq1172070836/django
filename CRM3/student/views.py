from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Student, StudentDetail, Grade, Course, Enroll

# Create your views here.

def base(request):
    return render(request, 'student/base.html')

def student_list(request):
    section = '学生列表'
    search = request.GET.get('search', '').strip()
    if search:
        if search.isdigit():
            stus = Student.objects.filter(Q(is_delete=0) & Q(qq=search) | Q(phone=search))
        else:
            stus = Student.objects.filter(is_delete=0, name=search)
    else:
        stus = Student.objects.filter(is_delete=0)

    stus = stus.order_by('-c_time')
    return render(request, 'student/student_list.html', context={
        'section': section,
        'stus': stus,
        'search': search,
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
        StudentDetail.objects.create(
            college=request.POST.get('college'),
            stu=stu,
        )
        return redirect('student:student_list')