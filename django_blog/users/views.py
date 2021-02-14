from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # Django's already made form
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    # When the request is submitted after filling out the form (As the POST request)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # This will save to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})