from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length = 100)
	content = models.TextField(max_length = 5000)
	author = models.CharField(max_length = 50)
	discription = models.CharField(max_length=150,null=True, blank=True)
	public_date = models.DateField()

class Picture(models.Model):
	title = models.CharField(max_length = 50)
	image = models.ImageField(upload_to = 'photos')


class About_us(models.Model):
	content = models.TextField(max_length = 5000)
	picture = models.ManyToManyField(Picture)
		
class Contact_us(models.Model):
	name = models.CharField(max_length = 50)
	company = models.CharField(max_length = 100)
	tel = models.IntegerField(max_length = 15)
	address = models.CharField(max_length = 100)
	web = models.URLField()
	email = models.EmailField()
	weibo = models.CharField(max_length = 30)
	weiboimg = models.ImageField(upload_to = 'photos')

class Cases(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	descriptions = models.CharField(max_length=150,null=True, blank=True)

class Anli(models.Model):
	title = models.CharField(max_length=50)
	case = models.ForeignKey(Cases,related_name='case')
	discriptions = models.CharField(max_length=150,null=True, blank=True)

class CateBlog(models.Model):
	title = models.CharField(max_length=50)
	blog = models.ForeignKey(Blog,related_name="blog")
	discriptions = models.CharField(max_length=150,null=True, blank=True)