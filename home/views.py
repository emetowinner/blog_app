from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from .forms import PostForm

def index(request):

    context = {
        'title':'Home'
    }
    return render(request,'home/index.html',context)

def about(request):
    context = {
        'title':'About'
    }
    return render(request,'home/about.html',context)
    
def blog(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
        'title':'Blog'
    }
    return render(request,'home/blog.html',context)

def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        filled_form = PostForm(request.POST)
        if filled_form.is_valid():
            title = filled_form.cleaned_data['title']
            content = filled_form.cleaned_data['content']
            user = User.objects.get(id=request.user.id)
            author = user
            post = Post(title=title,content=content,author=author)
            post.save()
            message = f'your post {title} has been submitted'

            context = {
            'title':'Create Post',
            'form':form,
            'message':message,
        }
            return render(request,'home/create-post.html',context)
        else:
            message = 'The for you submitted is not valid!'
            form = PostForm()
            context = {
            'title':'Create Post',
            'form':form,
            'message':message,
            }
            return render(request,'home/create-post.html',context)
    else:
        context = {
            'title':'Create Post',
            'form':form
        }
        return render(request,'home/create-post.html',context)


def user_post(request,username):
    context = {
        'title':'User Post'
    }
    return render(request,'home/user-post.html',context)