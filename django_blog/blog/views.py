from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post # . means from this folder
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

# Add 'LoginRequiredMixin' for redirecting user if not logged in for this view
class PostCreateView(LoginRequiredMixin, CreateView): 
    model = Post
    fields = ['title', 'content']

    # This tells who is the author of this post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# 'UserPassesTestMixin' for adding requirement
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, CreateView): 
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # This is the required test for 'UserPassesTestMixin' (To prevent users from updating other users post)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' # Go back to home if deleted successfully

    # This is the required test for 'UserPassesTestMixin' (To prevent users from deleting other users post)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})