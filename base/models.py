from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass
    

    




    #username = models.CharField(max_length=200, null=True, unique=True)
    #email = models.EmailField(unique=True, null=True)

    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = []

#avatar = models.ImageField(null=True, default="avatar.svg")
    

class data(models.Model):
    datestamp = models.DateTimeField(auto_now_add=True)
    timestamp = models.CharField(max_length=10)
    temperature = models.FloatField(null=True)
    rainfall = models.FloatField(null=True)
    humidity = models.FloatField(null=True)
    flowrate = models.FloatField(null=True)
    #FeedTemperature = 

def __init__(self):
    return self.temperature
    




