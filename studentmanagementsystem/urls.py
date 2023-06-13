from django.urls import path
from .views import StudentList,student_grades,student_details,student_fees,student_exam,TeacherList,teachers_std,teachers_sal

# urlpatterns = [
#     path('students/', StudentList.as_view(), name='student-list'),
#     path('students/<int:std_id>/', student_details, name='student_details'),
#     path('students/grades/<int:std_id>/', student_grades, name='student_grades'),

#  ]
urlpatterns = [path('students/', StudentList.as_view(), name='student-list'),
               path('students/grades/<int:std_id>/', student_grades, name='student_grades'),
               path('students/<int:std_id>/', student_details, name='student_details'),
               path('students/fees/<int:std_id>/', student_fees, name='student_fees'),
               path('students/exam/<int:std_id>/', student_exam, name='student_fees'),
               path('teachers/', TeacherList.as_view(), name='teacher-list'),
               path('teachers/<int:t_id>/', teachers_std, name='teacher-std'),
               path('teachers/salary/<int:t_id>/', teachers_sal, name='teacher-std'),]