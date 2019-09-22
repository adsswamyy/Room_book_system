from django.db import models

# Create your models here.

class accounts(models.Model):
    email=models.EmailField()
    username=models.CharField(max_length=30)
    Date_Joiend=models.DateField(auto_now_add=True)
    last_login=models.DateField(auto_now_add=True)
    password=models.CharField(max_length=30)
    confiem_password=models.CharField(max_length=30)
