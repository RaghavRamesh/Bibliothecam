from django.db import models

# Create your models here.
class Books(models.Model):
	title = models.CharField(max_length=150)
	author = models.CharField(max_length=100)
	pages = models.CharField(max_length=10)
	

	def __unicode__(self):
		return self.title + " / " + self.author + " / " + self.pages 



