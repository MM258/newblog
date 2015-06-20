from django.conf.urls import patterns,url
from blog import views

urlpatterns = patterns('',
	# url(r'^/$',views.home),
	url(r'^$',views.home),
	url(r'^blog/$',views.blog),
	url(r'^about_us/$',views.about_us),
	url(r'^contact_us/$',views.contact_us),
	url(r'^case/$',views.case),
	)