# Generated by Django 4.2.1 on 2023-06-07 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentmanagementsystem', '0002_alter_department_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'managed': False},
        ),
        migrations.AlterModelTable(
            name='student',
            table='student',
        ),
    ]
