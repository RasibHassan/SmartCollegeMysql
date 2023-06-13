from rest_framework import serializers
from .models import Student,Teacher
class StudentSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='d.depname', read_only=True)

    class Meta:
        model = Student
        fields = ['std_id','name','username', 'password','department']
class TeacherSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='d.depname', read_only=True)

    class Meta:
        model = Teacher
        fields = ['teacher','name','username','password','department']
