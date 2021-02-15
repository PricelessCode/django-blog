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
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def profile(request):
    return render(request, 'users/profile.html')
