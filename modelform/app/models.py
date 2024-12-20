from django.db import models

# Create your models here.
class teacher(models.Model):
    name=models.TextField()
    email=models.CharField(max_length=30)
    
class files(models.Model):
    file=models.FileField()
    description=models.CharField(max_length=30)