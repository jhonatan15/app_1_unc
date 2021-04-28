from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Subject(models.Model):
    name = models.CharField(max_length=30)

class Enrollment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)


class Note(models.Model):
    value = models.DecimalField(max_digits=5, decimal_places=2)
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE)
