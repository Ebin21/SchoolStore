# models.py
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=250, blank=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Purpose(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class StudentForm(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    mail_id = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)
    materials_provided = models.ManyToManyField(Material)

    def __str__(self):
        return self.name

    
    
# Create your models here.
#  class Student(models.Model):
    
#     GENDER_CHOICES = (
#             ('M', 'Male'),
#             ('F', 'Female'),
#             ('O', 'Other'),
#         )
    
#     DEPARTMENT_CHOICES = [
#         ('Commerce', 'Commerce'),
#         ('Medicine', 'Medicine'),
#         ('Computer', 'Computer'),
#         ('Maths', 'Maths'),
#         ('Arts','Arts'),
#     ]
    
#     COURSES_CHOICES = {
#         'Commerce': [('MBA', 'MBA'),('BBA', 'BBA'), ('BCom', 'BCom'),('MCom', 'MCom')],
#         'Medicine': [('MBBS', 'MBBS'), ('MD', 'MD')],
#         'Computer': [('BSc Computer', 'BSc Computer'), ('BCA', 'BCA')],
#         'Arts': [('BA', 'BA'), ('BFA', 'BFA')],
#         'Maths': [('BSc Maths', 'BSc Maths'), ('MSc Maths', 'MSc Maths')],
#     }

#     PURPOSE_CHOICES = [
#         ('Enquiry', 'Enquiry'),
#         ('Registration ', 'Registration'),
#         ('Get Information ', 'Get Information'),
        
#     ]
    
#     MATERIALS_CHOICES = [
#         ('NoteBook', 'NoteBook'),
#         ('Pen', 'Pen'),
#         ('Exam Papers', 'Exam Papers'),
#     ]
    
#     name =models.CharField(max_length=250, unique=True)
#     DOB=models.DateField()
#     age =models.IntegerField()
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     Phone =models.IntegerField()
#     email =models.CharField(max_length=250, unique=True)
#     address =models.CharField(max_length=500)
#     department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
#     course = models.CharField(max_length=10, choices=[], blank=True)
#     purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES)
#     materials_provide = models.CharField(max_length=50)

   

#     def __str__(self):
#              return self.name
         