from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import FeedbackForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string


# Create your views here.
@login_required
def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            note = 'Success'
            form.save()
            return render(request, 'templates/feedback.html', {'form':form, 'note':note})
    else:
        form = FeedbackForm()
    return render(request, 'templates/feedback.html', {'form': form})



def login_view(request):
    if request.method  == 'POST':        
        email = request.POST.get('email')
        password = request.POST.get('password')
        user =  authenticate(request, email=email, password=password)
        
        if user.is_authenticated:
            return redirect('/')

        if user is None:
            context = {"error": "Invalid email or password"}
            return render(request, 'templates/login.html', context)
        login(request,user)
        return redirect('/')
    return render(request, 'templates/signin.html', {})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    return render(request, 'templates/logout.html', {})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email = email, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful"))
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'templates/signup.html', {'form':form})


def faq(request):
    return render(request, "faq.html")

def pricing(request):
    return render(request, "pricing.html")

def index(request):
    return render(request, "index.html")

@login_required
def dashboard_view(request):
    content = render_to_string('createform.html', context=None)
    return HttpResponse(content)