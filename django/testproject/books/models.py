from django.db import models

# Create your models here.
class Books(models.Model):
	title = models.CharField(max_length=150)
	author = models.CharField(max_length=100)
	pages = models.IntegerField(max_length=10)
