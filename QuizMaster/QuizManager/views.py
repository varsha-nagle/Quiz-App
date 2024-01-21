from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CreateUserForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        # logger.info('User authentication result: %s', user)

        if user is not None:
            login(request, user)
            # Redirect to the desired page after login
            return redirect('/home')  # Check that 'home' matches your actual URL pattern
        else:
            # Handle invalid login
            if username and password:
                messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now login.')
            # Create a new instance of the form to clear input fields
            form = CreateUserForm()
            # Redirect to the desired page after registration
            return redirect('login')  # Replace 'login' with the name of your login URL pattern
        else:
            print(form.errors, 'Error block')
    else:
        form = CreateUserForm()
        form.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        form.fields['email'].widget.attrs['placeholder'] = 'Enter your email'

    return render(request, 'register.html', {'form': form})


def home_view(request):
    return render(request, 'home.html')


def rules_view(request):
    return render(request, 'rules.html')


def quest_view(request):
    return render(request, 'quest.html')
