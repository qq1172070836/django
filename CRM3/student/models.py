from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.SmallIntegerField(null=True)
    SET_CHOICES = (
        [0, '女'],
        [1, '男']
    )
    sex = models.SmallIntegerField(choices=SET_CHOICES, default=1)
    qq = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    c_time = models.DateTimeField(auto_now_add=True)
    grade = models.ForeignKey('Grade', on_delete=models.SET_NULL, null=True)
    is_delete = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name

class StudentDetail(models.Model):
    college = models.CharField(max_length=20)
    student = models.OneToOneField('Student', on_delete=models.CASCADE)

    def __str__(self):
        return self.college

class Grade(models.Model):
    name = models.CharField(max_length=20)
    num = models.CharField('班期', max_length=20)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=20)
    students = models.ManyToManyField('Student', through='Enroll')

    def __str__(self):
        return self.name

# 中间表
class Enroll(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    pay = models.FloatField('缴费金额', default=0)
    c_time = models.DateTimeField('报名时间', auto_now_add=True)
