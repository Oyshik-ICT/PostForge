from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Posts
from django.views.generic import ListView, DetailView, CreateView

posts = Posts.objects.all()

def home(request):
    return render(request, 'blog/home.html', {'posts': posts})

class PostListView(ListView):
    model = Posts
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Posts

class PostCreateView(CreateView):
    model = Posts
    fields = ['title', 'content']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})

