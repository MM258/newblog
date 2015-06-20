from django.conf.urls import patterns,url
from blog import views
from blog.views import *

urlpatterns = patterns('views',
	# url(r'^/$',views.home),
	url(r'^$',home),
	url(r'^index/$',index.as_view(),name="index"),
	url(r'^blog/$',blog),
	url(r'^about_us/$',views.about_us),
	url(r'^contact_us/$',contact_us),
	url(r'^case/$',case),
	)