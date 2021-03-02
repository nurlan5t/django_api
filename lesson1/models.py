from django.db import models

from django.db.models import SET_NULL


class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50, null=True)
    price = models.IntegerField(null=True)
    level = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    course = models.ForeignKey(Course, null=True, on_delete=SET_NULL)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name