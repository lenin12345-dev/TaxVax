from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# this is the new comment added from mac lets see if it works

def index(request):
    return HttpResponse('hello world')
