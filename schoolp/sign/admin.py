from django.contrib import admin
from . models import Department,Course,Material,Purpose,StudentForm

# Register your models here.
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Material)
admin.site.register(Purpose)
admin.site.register(StudentForm)
