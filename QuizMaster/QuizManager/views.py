from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CreateUserForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_view(request):
    # if request.method == 'POST':
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     user = authenticate(request, email=email, password=password)
    #     # if user is not None:
    #     #     login(request, user)
    #     #     # Redirect to the desired page after login
    #     #     return redirect('index')  # Check that 'home' matches your actual URL pattern
    #     # else:
    #     #     # Handle invalid login
    #     #     pass
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # Create a new instance of the form to clear input fields
            form = CreateUserForm()
            print('Data is saved')
            # Redirect to the desired page after registration
            return redirect('login')  # Replace 'login' with the name of your login URL pattern
        else:
            print(form.errors, 'Error block')
    else:
        form = CreateUserForm()

    return render(request, 'register.html', {'form': form})