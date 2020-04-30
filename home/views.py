from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'home/about.html', context)


def blog(request):
    posts = Post.objects.all().order_by('-date_posted')
    context = {
        'posts': posts,
        'title': 'Blog'
    }
    return render(request, 'home/blog.html', context)


@login_required(login_url='login')
def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        filled_form = PostForm(request.POST)
        if filled_form.is_valid():
            title = filled_form.cleaned_data['title']
            content = filled_form.cleaned_data['content']
            user = User.objects.get(id=request.user.id)
            author = user
            post = Post(title=title, content=content, author=author)
            post.save()
            message = f'your post {title} has been submitted'

            context = {
                'title': 'Create Post',
                'form': form,
                'message': message,
            }
            return render(request, 'home/create-post.html', context)
        else:
            message = 'The for you submitted is not valid!'
            form = PostForm()
            context = {
                'title': 'Create Post',
                'form': form,
                'message': message,
            }
            return render(request, 'home/create-post.html', context)
    else:
        context = {
            'title': 'Create Post',
            'form': form
        }
        return render(request, 'home/create-post.html', context)

class PostsDetailView(DetailView):
    model = Post
    #template_name = 'home/post-details.html'

def post_update(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,'Post updated successfully')
            return render(request,'home/post_update.html',{'form':form})
    else:
        form = PostForm(instance=post)
        messages.error(request,'Something went wrong try again')
        return render(request,'home/post_update.html',{'form':form})

def user_post(request, username):
    context = {
        'title': 'User Post'
    }
    return render(request, 'home/user-post.html', context)
