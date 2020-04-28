from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def register(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Welcome {request.user}, registrtion was successful')            
            return redirect('login')
        else:
            message = 'sorry something went wrong!'
            context = {
            'title':'Register',
            'form':form,
            'message':message
            }
            return render(request,'users/register.html',context)
    else:
        form = UserRegistrationForm()
        context = {
            'title':'Create Post',
            'form':form
        }
        return render(request,'users/register.html',context)
@login_required(login_url='login')
def profile(request):
    context = {
        'title':'Profile'
    }
    return render(request,'users/profile.html',context)