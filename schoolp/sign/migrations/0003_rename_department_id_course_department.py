# Generated by Django 4.2.2 on 2023-12-09 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0002_rename_department_course_department_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='department_id',
            new_name='department',
        ),
    ]
