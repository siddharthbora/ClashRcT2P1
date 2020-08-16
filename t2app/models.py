from django.db import models
from django.contrib.auth.models import User


class Sid(models.Model):
    Name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phoneNo = models.CharField(max_length=11)
    gender = models.CharField(max_length=6)


class Prof(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    phone = models.CharField(max_length=11, null=False, blank=False)

    def __str__(self):
        return self.Name
