from multiprocessing import context
import re
from django.shortcuts import render, redirect
from .models import Blog_post
from .forms import *
from django.contrib.auth import logout

def home(request):
    context = {'blogs': Blog_post.objects.all()}
    return render(request,'home.html', context)

#To Add your Blogs
def add_blog(request):
    
    #handling post requests
        #getting  data from post request
    form = Add_Form()
    if request.method == 'POST':
        form = Add_Form(request.POST, request.FILES)
        
        if form.is_valid():
            #content = form.cleaned_data['content']
            form_save = form.save(commit=False)
            form_save.user = request.user
            form.save()          
            return redirect('/add_blog/')
    context = {'form' : form}
    return render(request, 'add_blog.html', context)

#See full Blog with details
def blogDetail(request, slug):
    context = {}
    try:
        blog_obj = Blog_post.objects.filter(slug = slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request,'blogDetail.html', context)

#to view and edit blogs
def editBlog(request):
    context = {}
    try:
        blog_obj2 = Blog_post.objects.filter(user = request.user)
        context['blog_obj2'] = blog_obj2
    except Exception as e:
        print(e)
    return render(request,'editBlog.html',context)

#for deleting blogs
def blogDelete(request, id):
    try:
        blog_obj = Blog_post.objects.get(id = id)
        if blog_obj.user == request.user:
            blog_obj.delete()
    except Exception as e:
        print(e)
    return redirect('/editBlog')

#update blogs
def blogUpdate(request, slug):
    context = {}
    try:
        blog_obj = Blog_post.objects.get(slug = slug)
        if blog_obj.user != request.user:
            return redirect('/')

        initial_dict = {'title':blog_obj.title, 'content': blog_obj.content}
        form = Add_Form(initial = initial_dict) # getting initial values

        if request.method == 'POST':
            form = Add_Form(request.POST, request.FILES)
        
        if form.is_valid():
            #content = form.cleaned_data['content']
            form_save = form.save(commit=False)
            form_save.user = request.user
            form.save()

        context['blog'] = blog_obj
        context['form'] = form
    except Exception as e:
        print(e)
    return render(request,'updateBlog.html',context)

#user login page
def login_auth(request):
    return render(request,'login.html')

def logout_auth(request):
    logout(request)
    return redirect('/')

#user signup page
def sign_up(request):
    return render(request,'signup.html')
    





