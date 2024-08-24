from django.db import models

class Person(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    resume=models.FileField(upload_to='files/')

# Create your models here.
