from django.shortcuts import render
from .models import Posts

posts = Posts.objects.all()

def home(request):
    return render(request, 'blog/home.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})

