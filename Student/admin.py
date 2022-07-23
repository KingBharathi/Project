from django.contrib import admin
from Student.models import Student
from Student.models import StudentMarks

# Register your models here.
class StudentData(admin.ModelAdmin):
    stud_details=['StudId', 'StudName', 'StudPhone']

admin.site.register(Student, StudentData)

class StudentMarkAdmin(admin.ModelAdmin):
    stud_marks=['StudId', 'StudName2', 'Mark01', 'Mark02', 'Mark03']

admin.site.register(StudentMarks, StudentMarkAdmin)