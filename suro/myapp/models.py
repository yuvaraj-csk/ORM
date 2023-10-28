from django.db import models
from django.contrib import admin
class Football(models.Model):
    name=models.CharField(max_length=100)
    jid=models.IntegerField()
    coach=models.CharField(max_length=100)
    age=models.IntegerField()
    number=models.IntegerField()

class FootballAdmin(admin.ModelAdmin):
    list_display=('name','jid','coach','age','number')

# Create your models here.
