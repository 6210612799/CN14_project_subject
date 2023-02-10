from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Subject(models.Model):
    S_id = models.CharField(max_length=25)
    S_name = models.CharField(max_length=50)
    S_credits = models.FloatField()
    S_detail = models.TextField()
    S_teacher = models.ForeignKey(Person, on_delete=models.CASCADE)