from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# this is the new comment added from mac lets see if it works
# this is the comment added on windows
def index(request):
    return HttpResponse('hello world')
# this is a simple comment added to views
def user_list(request):
	return