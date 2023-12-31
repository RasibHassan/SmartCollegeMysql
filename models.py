# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Examination(models.Model):
    c = models.OneToOneField('Course', models.DO_NOTHING, primary_key=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    venue = models.CharField(db_column='Venue', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Examination'


class Fees(models.Model):
    s = models.OneToOneField('Student', models.DO_NOTHING, primary_key=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Fees'


class Salary(models.Model):
    teacherid = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='teacherid')
    salaryid = models.IntegerField(primary_key=True)
    months = models.CharField(db_column='Months', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ammount = models.IntegerField(db_column='Ammount', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Salary'


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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class Department(models.Model):
    d_id = models.IntegerField(primary_key=True)
    depname = models.CharField(db_column='Depname', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class Student(models.Model):
    std_id = models.IntegerField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    d = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'
