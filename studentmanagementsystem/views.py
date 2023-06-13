from django.http import HttpResponse
from rest_framework import generics
from .models import Student,Department,Grades,Course,Coursedetails,Fees,Examination,Teacher,Salary
from .serializers import StudentSerializer,TeacherSerializer
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()

    serializer_class = StudentSerializer

        # Retrieve the StudentDetails object associated with the Student



def student_grades(request, std_id):
    # Retrieve the Student object based on the provided username
    student = get_object_or_404(Student, std_id=std_id)

    # Retrieve the StudentDetails object associated with the Student
    student_grades = get_object_or_404(Grades,s=student)
    data1=[
    {
        "grade": "GPA",

        "gpa1": student_grades.gpa1

    },
    {
        "grade": "GPA2",

        "gpa2": student_grades.gpa2

    },
    {
        "grade": "GPA3",

        "gpa3": student_grades.gpa3

    },  {
        "grade": "GPA4",

        "gpa4": student_grades.gpa4

    },
    {
        "grade": "CGPA",

        "cgpa": student_grades.cgpa

    },
    ]
    

    return JsonResponse(data1, safe=False)

def student_details(request, std_id):
    # Retrieve the Student object based on the provided username
    student = get_object_or_404(Student, std_id=std_id)

    # Retrieve the StudentDetails object associated with the Student
    student_details = Coursedetails.objects.filter(s=student)

    # Serialize the data to JSON and return it as a response
    print(student_details)
    data = []
    for data_obj in student_details:
        percentage=(data_obj.attendance/40)*100
        data.append({
            'course': data_obj.c.cname,
            'attendance_percentage':percentage,
            'total_attendance':40,
            'attendance': data_obj.attendance,
            'total_marks':20,
            'mid_marks': data_obj.marks,
            "semester": "Spring 2023",

        })
    return JsonResponse(data, safe=False)
def student_fees(request, std_id):
    # Retrieve the Student object based on the provided username
    student = get_object_or_404(Student, std_id=std_id)

    # Retrieve the StudentDetails object associated with the Student
    student_fee = get_object_or_404(Fees,s=student)
    data=[
        {
            'amount':student_fee.amount,
            'status':student_fee.status
        }
    ]
    return JsonResponse(data, safe=False)

def student_exam(request, std_id):
    # Retrieve the Student object based on the provided username
    coursedetail = Coursedetails.objects.filter(s_id=std_id)
    
    # Retrieve the Course IDs from the Coursedetails objects
    course_ids = coursedetail.values_list('c_id', flat=True)
    
    # Retrieve the examinations associated with the Course IDs
    exam = Examination.objects.filter(c_id__in=course_ids)
    # Retrieve the StudentDetails object associated with the Student
    data=[]
    for data_obj in exam:
        data.append({
            "coursename":data_obj.c.cname,
            "date":data_obj.date,
            "time":data_obj.time,
            "venue":data_obj.venue,
        })
    return JsonResponse(data, safe=False)
class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()

    serializer_class = TeacherSerializer

        # Retrieve the StudentDetails object associated with the Student
def teachers_std(request, t_id):
    # Retrieve the Student object based on the provided username
    teacher = get_object_or_404(Teacher,teacher=t_id)
    
    # Retrieve the Course IDs from the Coursedetails objects
    stds = Coursedetails.objects.filter(c=teacher.c)
    
    # Retrieve the examinations associated with the Course IDs
    data=[]
    for data_obj in stds:
        data.append({
            "std_id":data_obj.s.std_id,
            "name":data_obj.s.name
        })
           # Retrieve the StudentDetails object associated with the Student
    return JsonResponse(data, safe=False)
def teachers_sal(request, t_id):
    # Retrieve the Student object based on the provided username
    teachers = get_object_or_404(Teacher,teacher=t_id)
    salary = Salary.objects.filter(teacherid=teachers.teacher)
    data=[]
    for i in salary:
        data.append({
            "months":i.months,
            "amount":i.ammount,
            "status":i.status
        })
    return JsonResponse(data, safe=False)
