from django.db import models


# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
    phone_no = models.IntegerField()
    age = models.IntegerField()

