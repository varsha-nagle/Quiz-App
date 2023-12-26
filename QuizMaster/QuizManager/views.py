from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


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
