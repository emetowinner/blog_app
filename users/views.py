from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Users
from django.contrib.auth.models import User
from django.contrib.auth import login,logout




def register(request):
    form = Users()
    if request.method == 'POST':
        filled_form = Users(request.POST)
        if filled_form.is_valid():
            login(request)
            message = f'Welcome {request.user}, login was successful'
            context = {
                'title':'Blog',
                'message':message
            }
            return redirect('users/blog',context)
        else:
            message = 'The for you submitted is not valid!'
            form = Users()
            context = {
            'title':'Register',
            'form':form,
            'message':message,
            }
            return render(request,'users/register.html',context)
    else:
        context = {
            'title':'Create Post',
            'form':form
        }
        return render(request,'users/register.html',context)

def logout(request):
    context = {
        'title':'logout'
    }
    return render(request,'users/logout.html',context)

def profile(request):
    context = {
        'title':'Profile'
    }
    return render(request,'users/profile.html',context)

def login(request):
    context = {
        'title':'Login'
    }
    return render(request,'users/login.html',context)
