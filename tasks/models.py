from django.db import models

# Create your models here.

class Task(models.Model):
    titel = models.CharField(max_length=100)
    descripccion = models.TextField(blank=True)