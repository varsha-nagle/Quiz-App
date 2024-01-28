from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CreateUserForm
from .models import Question


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


# def quiz_page(request):
#     # Get the current question ID from the session or default to the first question
#     current_question_id = request.session.get('current_question_id', None)
#     if current_question_id is None:
#         questions = Question.objects.all()
#         if questions:
#             current_question_id = questions.first().id
#             request.session['current_question_id'] = current_question_id
#
#     # Get the current question based on the current_question_id
#     current_question = Question.objects.get(id=current_question_id)
#
#     # Handle form submission if any
#     if request.method == 'POST':
#         # Process the submitted answer and update the session
#         submitted_answer = request.POST.get(f'question{current_question_id}', None)
#         # Add your answer processing logic here
#
#         # Move to the next question or finish the quiz based on your logic
#         # For example, move to the next question:
#         next_question = Question.objects.filter(id__gt=current_question_id).first()
#         if next_question:
#             request.session['current_question_id'] = next_question.id
#             return redirect('quiz_page')
#         else:
#             # Redirect to a quiz completion page or wherever you want to go after the last question
#             return redirect('quiz_complete')
#
#     return render(request, 'quiz_page.html', {'current_question': current_question})


def quiz_page(request):
    current_question_index = request.session.get('current_question_index', 0)
    questions = Question.objects.all()

    if current_question_index >= len(questions):
        # Redirect to a quiz completion page or wherever you want to go after the last question
        return redirect('quiz_complete')

    current_question = questions[current_question_index]
    last_question_index = len(questions) - 1

    if request.method == 'POST':
        # Process the submitted answer and update the session
        submitted_answer = request.POST.get(f'question{current_question.id}', None)
        # Add your answer processing logic here

        # Determine whether it's "Next" or "Previous" based on the button clicked
        if 'next' in request.POST:
            current_question_index += 1
        elif 'previous' in request.POST:
            current_question_index -= 1

        request.session['current_question_index'] = current_question_index
        return redirect('quiz_page')

    return render(request, 'quiz_page.html', {'current_question': current_question, 'total_questions': len(questions), 'current_question_index': current_question_index, 'last_question_index': last_question_index})



