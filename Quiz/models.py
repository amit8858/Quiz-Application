from django.db import models

# Create your models here.

class History(models.Model):
    Question = models.CharField(max_length=100)
    Option1 = models.CharField(max_length=100)
    Option2 = models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100)
    Option4 = models.CharField(max_length=100)
    Corrans = models.CharField(max_length=100)

class Geography(models.Model):
    Question = models.CharField(max_length=200)
    Option1 = models.CharField(max_length=200)
    Option2 = models.CharField(max_length=200)
    Option3 = models.CharField(max_length=200)
    Option4 = models.CharField(max_length=200)
    Corrans = models.CharField(max_length=200)

class Science(models.Model):
    Question = models.CharField(max_length=100)
    Option1 = models.CharField(max_length=100)
    Option2 = models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100)
    Option4 = models.CharField(max_length=100)
    Corrans = models.CharField(max_length=100)