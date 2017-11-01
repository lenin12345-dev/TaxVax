from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import UserBio, UserTaxInfo
# Create your views here.
# this is the new comment added from mac lets see if it works
# this is the comment added on windows
def index(request):
    return HttpResponse('hello world')
# this is a simple comment added to views
def display_user_list(request):
	user_list = UserBio.objects.all()
	template = loader.get_template('home/user_list.html')
	context ={
		'user_list': user_list,
	}

	return HttpResponse(template.render(context,request))
	
def display_user_details(request, user_id):
	user_detail = UserTaxInfo.objects.get(pk=user_id)
	context ={
		'user_detail': user_detail,
	}
	template = loader.get_template('home/user_detail.html')
	return HttpResponse(template.render(context,request))

