from django.db import models

# Create your models here.
class Books(models.Model):
	title = models.CharField(max_length=150)
	author = models.CharField(max_length=100)
	pages = models.CharField(max_length=10)
	isbn = models.CharField(max_length=10)
	



