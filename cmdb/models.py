from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user=models.CharField(max_length=32)
    pwd=models.CharField(max_length=32)
    number=models.CharField(max_length=32)
class test(models.Model):
    test1=models.CharField(max_length=32)
class test2(models.Model):
    test2=models.CharField(max_length=32)