from django.db import models
#
from simple_search import search_form_factory

# Create your models here
class sms(models.Model):
    name =models.CharField(max_length=20)
    message=models.TextField(max_length=500)
    ph_no=models.IntegerField()
    username=models.CharField(max_length=15)
    password=models.IntegerField()

SearchForm = search_form_factory(sms.objects.all(),
                                 ['name', 'ph_no'])
class sms_login(models.Model):
    username = models.CharField(max_length=20)
    password = models.IntegerField()