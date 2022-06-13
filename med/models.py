from django.db import models

class Doctors(models.Model):
    name= models.CharField(max_length=30)
    gender= models.CharField(max_length=10)
    expert= models.TextField()
    rating= models.IntegerField()
    location= models.TextField()
    price= models.IntegerField()