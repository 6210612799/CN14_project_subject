from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    def __str__(self):
        return self.first_name
class Subject(models.Model):
    S_id = models.CharField(max_length=25)
    S_name = models.CharField(max_length=50)
    S_credits = models.FloatField()
    S_detail = models.TextField()
    S_teacher = models.ForeignKey(Person, on_delete=models.CASCADE)
    def __str__(self):
        return self.S_name

class Student(models.Model):
    student_id = models.TextField()
    student_subject =  models.ForeignKey(Subject, on_delete=models.CASCADE)
    student_temp = models.ManyToManyField(
        Subject, blank=True, related_name="student_temp")
    def __str__(self):
        return f"{self.student_id} "