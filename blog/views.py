from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
#ListView representa una lista de objects
from .models import Post

# Create your views here.
# class subclase(clase):
class BlogListView(ListView):
  model = Post
  template_name = 'home.html'

class BlogDetailView(DetailView):
  model = Post
  template_name = 'post_detail.html'

class BlogCreateView(CreateView):
  model = Post
  template_name = 'post_new.html'
  fields = '__all__'
