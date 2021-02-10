from django.shortcuts import render

posts = [
    {
        'author': 'Seungho Lee',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date': 'Feb 10, 2021'
    },
    {
        'author': 'Matt Lee',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date': 'Feb 10, 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})