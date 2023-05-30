from pyexpat import model
from django.db import models

# Create your models here.

class Question(models.Model):
    quno=models.IntegerField(primary_key=True, auto_created=True)
    que=models.CharField(max_length=400)
    optiona=models.CharField(max_length=100)
    optionb=models.CharField(max_length=100)
    optionc=models.CharField(max_length=100)
    optiond=models.CharField(max_length=100)
    answer=models.CharField(max_length=1)
class User(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    fullname=models.CharField(max_length=40)
    password=models.CharField(max_length=10)
    role=models.CharField(max_length=15)


class Result(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    total_attempt=models.IntegerField()
    total_wrong=models.IntegerField()
    total_right=models.IntegerField()
    date=models.DateField(null=False, blank=False, auto_now=True,
    verbose_name=u'Fecha de última modificación')
