from .models import Student,Department,Grades,Course,Coursedetails,Fees,Examination,Teacher
from django.contrib import admin
@admin.register(Department)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('d_id','depname')
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('std_id','username', 'password')
@admin.register(Grades)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('s_id','cgpa','gpa1','gpa2','gpa3','gpa4')

@admin.register(Course)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('c_id','cname')
@admin.register(Coursedetails)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('s_id','c_id','attendance','marks')   

@admin.register(Fees)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('s_id','amount','status')

@admin.register(Examination)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('c_id','date','time','venue')
@admin.register(Teacher)
class StudentssAdmin(admin.ModelAdmin):
    list_display = ('teacher','name','username','password')
# @admin.register(StudentData)
# class StudenetDataAdmin(admin.ModelAdmin):
#     list_display = ('student','course','attendance','marks')
# @admin.register(Grades)
# class GradesDataAdmin(admin.ModelAdmin):
#     list_display = ('student','cgpa','gpa1','gpa2','gpa3','gpa4')