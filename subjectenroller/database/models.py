from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel, TreeForeignKey
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
    pre_id = models.ManyToManyField(
        'self', blank=True, symmetrical=False, related_name='presub')
    post_id = models.ManyToManyField(
        'self', blank=True, symmetrical=False, related_name='postsub')
    def __str__(self):
        return self.S_id

class Student(models.Model):
    student_id = models.TextField()
    student_subject =  models.ForeignKey(Subject, on_delete=models.CASCADE)
    student_temp = models.ManyToManyField(
        Subject, blank=True, related_name="student_temp")
    def __str__(self):
        return f"{self.student_id} "
    
class Skill(MPTTModel):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    lft = models.PositiveIntegerField(editable=False, db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.subject.S_id

    def save(self, *args, **kwargs):
        # set default value for lft
        if not self.lft:
            self.lft = 0
        super().save(*args, **kwargs)

    


