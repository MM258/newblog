from django.shortcuts import render_to_response
from blog.models import *
from django.template import RequestContext
# Create your views here.

def home(request):
	# contact = Contact_us.objects.all()
	# return render_to_response('home.html',{"posts":contact},context_instance = RequestContext(request))
	
	return render_to_response('home.html','',context_instance = RequestContext(request))

def blog(request):
	
	blog = Blog.objects.all()
	return render_to_response("blog.html",{"blog": blog},context_instance=RequestContext(request))

def case(request):
	import ipdb;
	ipdb.set_trace()
	# case = Case.objects.all()
	case_id = int(request.GET.get('case_id',0))
	if case_id == 0:
		case_demo = Case.objects.filter(id=case_id)
	else:
		case_demo = Case.objects.all()
	return render_to_response('case.html',{"case":case_demo},context_instance = RequestContext(request))

# def jinji(request):
# 	jinji = Case.Jinji.all()
# 	# import ipdb;
# 	# ipdb.set_trace()
# 	return render_to_response('anjian/jinji.html',{"case":jinji},context_instance = RequestContext(request))

def about_us(request):
	about = About_us.objects.all()
	return render_to_response('about_us.html',{"about":about},context_instance = RequestContext(request))

def contact_us(request):
	contact = Contact_us.objects.all()
	return render_to_response('contact_us.html',{"posts":contact},context_instance = RequestContext(request))
	
