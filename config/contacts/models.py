from django.db import models

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)