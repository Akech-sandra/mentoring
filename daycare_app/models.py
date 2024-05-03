from django.db import models
from django.utils import timezone

# Create your models here.

class Login(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.email
    
class Signup(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirmPass = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name    