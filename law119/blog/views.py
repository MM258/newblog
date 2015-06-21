from django.shortcuts import render_to_response
from blog.models import *
from django.template import RequestContext
from django.views.generic.base import TemplateView

import datetime

# Create your views here.
class index(TemplateView):
	template_name = 'blog/home.html'
	def get_context_data(self,**kwargs):
		# today = datetime.datetime.today()
		blogcate = CateBlog.objects.all()
		anli = Anli.objects.all()
		# visitors = center.visitor_set.filter(date__range=(date_from,date_to)).order_by('-date')
		context_data = super(index,self).get_context_data(**kwargs)
		context_data['blogcate'] = blogcate
		context_data['anli'] = anli
		return context_data



def home(request):
	# contact = Contact_us.objects.all()
	# return render_to_response('home.html',{"posts":contact},context_instance = RequestContext(request))

	return render_to_response('home.html','',context_instance = RequestContext(request))

def blog(request):
	
	blog = Blog.objects.all()
	return render_to_response("blog.html",{"blog": blog},context_instance=RequestContext(request))

def case(request):
	# case = Case.objects.all()
	case_id = int(request.GET.get('case_id',0))
	if case_id == 0:
		case_demo = Cases.objects.filter(id=case_id)
	else:
		case_demo = Cases.objects.all()
	return render_to_response('case.html',{"case":case_demo},context_instance = RequestContext(request))

def about_us(request):
	about = About_us.objects.all()
	return render_to_response('about_us.html',{"about":about},context_instance = RequestContext(request))

def contact_us(request):
	contact = Contact_us.objects.all()
	return render_to_response('contact_us.html',{"posts":contact},context_instance = RequestContext(request))
	
