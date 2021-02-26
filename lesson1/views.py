import serializer as serializer
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
import json
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student

# Create your views here.
def get_students(request):
    students = Student.objects.all()
    list_student = []
    for i in students:
        list_student.append(model_to_dict(i))
    json_data = json.dumps({'list': list_student})
    return HttpResponse(json_data)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

@api_view(['GET'])
def get_drf_students(request):
    students = Student.objects.all()
    data = StudentSerializer(students, many=True).data
    return Response(data=data)

@api_view(['GET'])
def get_drf_student(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(data={'result': 'Student not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = StudentSerializer(student, many=False).data
    return Response(data=data, status=status.HTTP_200_OK)