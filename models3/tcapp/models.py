from django.db import models

# Create your models here.

class tcastudent(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="image/")
    resume=models.FileField(upload_to="files/")
