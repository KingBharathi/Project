from django.db import models

# Create your models here.
class Student(models.Model):
	StudId = models.CharField(max_length=5)
	StudName = models.CharField(max_length=20)
	StudPhone = models.CharField(max_length=10)

def __str__(self):
	return "STUDENT"+StudName


class StudentMarks(models.Model):
	StudId = models.CharField(max_length = 5)
	StudName2 = models.CharField(max_length = 20)
	Mark01 = models.CharField(max_length = 5)
	Mark02 = models.CharField(max_length = 5)
	Mark03 = models.CharField(max_length = 5)

def __str__(self):
	return "STUDENT"+StudName2
