from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post # . means from this folder

# Function based view
# def home(request):
#     context = {  
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)

# Class based View
class PostListView(ListView):
    model = Post # Which model to query
    template_name = 'blog/home.html' # if you don't add this, the class will look for <app>/<model>_<viewtype>.html which I don't have
    context_object_name = 'posts' # If you don't set this, you have to use name 'object' instead of 'posts' in the html template
    ordering = ['-date_posted'] # -date_posted mean reversed ordering of date_posted so that newest post is on the bottom

# Class based View
class PostDetailView(DetailView):
    model = Post

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})