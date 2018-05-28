from django.db import models

# Create your models here.
class user(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=20)
    utext = models.CharField(max_length=50,default='  ')
    uemail = models.CharField(max_length=20,default='  ')
    uaddress = models.CharField(max_length=40,default='  ')