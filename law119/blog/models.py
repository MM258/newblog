import os
from django.db import models
# from settings import MEDIA_ROOT
# from django.utils.translation import ugettext as _
# from django.db.models.fields.files import ImageFieldFile
# from utils import make_thumb
# from pulog.models import Post

# UPLOAD_ROOT = 'upload'
# THUMB_ROOT = 'upload/thumb'

# class Media(models.Model):
#     title = models.CharField(max_length = 120)
#     image = models.ImageField(upload_to = UPLOAD_ROOT)
#     thumb = models.ImageField(upload_to = THUMB_ROOT, blank = True)
#     date = models.DateTimeField(auto_now_add = True)
#     post = models.ForeignKey(Post)

#     class Meta:
#         verbose_name_plural = _('Media')

#     def save(self):
#         base, ext = os.path.splitext(os.path.basename(self.image.path))
#         thumb_pixbuf = make_thumb(os.path.join(MEDIA_ROOT, self.image.name))
#         relate_thumb_path = os.path.join(THUMB_ROOT, base + '.thumb' + ext)
#         thumb_path = os.path.join(MEDIA_ROOT, relate_thumb_path)
#         thumb_pixbuf.save(thumb_path)
#         self.thumb = ImageFieldFile(self, self.thumb, relate_thumb_path)
#         super(Media, self).save()

#     def __unicode__(self):
#         return _('%s, uploaded at %s') % (self.title, self.date.strftime('%T %h %d, %Y'))




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