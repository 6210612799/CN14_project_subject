from django.contrib import admin
from .models import Person , Subject , Student , Skill
# Register your models here.
admin.site.register(Person)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Skill)