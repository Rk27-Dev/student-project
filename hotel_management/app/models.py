from django.db import models

# Create your models here.
class register(models.Model):
    name=models.CharField(max_length=20)
    phone_number=models.IntegerField()
    email=models.EmailField()
    perpose=models.TextField(max_length=5000)

# class rooms(models.Model):
