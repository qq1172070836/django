from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.SmallIntegerField()
    sex = models.SmallIntegerField(max_length=1)
    qq = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

