# Generated by Django 4.2.2 on 2023-12-09 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0004_merge_20231209_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentform',
            name='course',
        ),
        migrations.RemoveField(
            model_name='studentform',
            name='department',
        ),
        migrations.RemoveField(
            model_name='studentform',
            name='materials_provided',
        ),
        migrations.RemoveField(
            model_name='studentform',
            name='purpose',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.DeleteModel(
            name='Purpose',
        ),
        migrations.DeleteModel(
            name='StudentForm',
        ),
    ]
