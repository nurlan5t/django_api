from rest_framework import serializers
from .models import Student, Course

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = 'id name count'.split()

    def get_count(self, obj):
        count = Student.objects.filter(course_id=obj.id).count()
        return count
