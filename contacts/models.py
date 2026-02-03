from django.db import models

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)   # 👈 CHANGE THIS
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name




