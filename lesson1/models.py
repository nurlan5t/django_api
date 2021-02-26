from django.db import models

from django.db.models import SET_NULL


class Course(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    course = models.ForeignKey(Course, null=True, on_delete=SET_NULL)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def str(self):
        return self.name
