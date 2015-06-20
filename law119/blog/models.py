from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length = 100)
	content = models.TextField(max_length = 5000)
	author = models.CharField(max_length = 50)
	public_date = models.DateField()

class Picture(models.Model):
	title = models.CharField(max_length = 50)
	image = models.ImageField(upload_to = 'photos')

class Jinji(models.Model):
	title = models.CharField(max_length = 30)
	content = models.TextField(max_length = 5000)
	pictures = models.ManyToManyField(Picture)

class Xinshi(models.Model):
	title = models.CharField(max_length = 30)
	content = models.TextField(max_length = 5000)
	pictures = models.ManyToManyField(Picture)	
	
class Case(models.Model):
	jinjis = models.ManyToManyField(Jinji)
	xinshis = models.ManyToManyField(Xinshi)
	LeiXing = models.CharField(max_length = 1,choices = (('J','jinji'),('X','xinshis')))

class About_us(models.Model):
	content = models.TextField(max_length = 5000)
	picture = models.ManyToManyField(Picture)
		
class Contact_us(models.Model):
	name = models.CharField(max_length = 50)
	company = models.CharField(max_length = 100)
	tel = models.CharField(max_length = 15)
	web = models.URLField()
	email = models.EmailField()
	weibo = models.CharField(max_length = 30)
