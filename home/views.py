from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('index page')

def about(request):
    return HttpResponse('about page')
    
def blog(request):
    return HttpResponse('blog page')

def login(request):
    return HttpResponse('login page')

def logout(request):
    return HttpResponse('logout page')

def profile(request):
    return HttpResponse('profle page')

