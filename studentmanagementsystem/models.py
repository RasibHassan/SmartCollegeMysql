
from django.db import models


class Department(models.Model):
    d_id = models.IntegerField(primary_key=True)
    depname = models.CharField(db_column='Depname', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'department'

class Student(models.Model):
    std_id = models.IntegerField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    d = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'
class Grades(models.Model):
    idgrades = models.AutoField(db_column='idGrades', primary_key=True)  # Field name made lowercase.
    s = models.ForeignKey('Student', models.DO_NOTHING, blank=True, null=True)
    cgpa = models.FloatField(blank=True, null=True)
    gpa1 = models.FloatField(blank=True, null=True)
    gpa2 = models.FloatField(blank=True, null=True)
    gpa3 = models.FloatField(blank=True, null=True)
    gpa4 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grades'
class Course(models.Model):
    c_id = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'course'


class Coursedetails(models.Model):
    s = models.OneToOneField('Student', models.DO_NOTHING, primary_key=True)  # The composite primary key (s_id, c_id) found, that is not supported. The first column is selected.
    c = models.ForeignKey(Course, models.DO_NOTHING)
    attendance = models.IntegerField(blank=True, null=True)
    marks = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coursedetails'
        unique_together = (('s', 'c'),)
class Fees(models.Model):
    s = models.OneToOneField('Student', models.DO_NOTHING, primary_key=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Fees'

class Examination(models.Model):
    c = models.ForeignKey('Course', models.DO_NOTHING, primary_key=True,unique=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    venue = models.CharField(db_column='Venue', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Examination'


class Teacher(models.Model):
    teacher = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    username = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=8, blank=True, null=True)
    c = models.ForeignKey('Course', models.DO_NOTHING, blank=True, null=True)
    d = models.ForeignKey('Department', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Teacher'
        
class Salary(models.Model):
    teacherid = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='teacherid')
    salaryid = models.IntegerField(primary_key=True)
    months = models.CharField(db_column='Months', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ammount = models.IntegerField(db_column='Ammount', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Salary'