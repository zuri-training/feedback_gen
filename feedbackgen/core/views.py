from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import FeedbackForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string




# # Create your views here.
# @login_required
# def feedback_form(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)

#         if form.is_valid():
#             note = 'Success'
#             form.save()
#             return render(request, 'templates/feedback.html', {'form':form, 'note':note})
#     else:
#         form = FeedbackForm()
#     return render(request, 'core/createform.html', {'form': form})



def signup_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pswrd']
        email=request.POST['email']
        confirm_password=request.POST['Confirm_pswrd']
       

        if User.objects.filter(username=username):
            messages.error(request,'Username already Exists!')
            return redirect('')


        if password!=confirm_password:
            messages.error(request,'Passwords do not match')
            return redirect('')

        # if len(username)>15:
        #     messages.error(request,'Usernames should not have more than 15 characters')
        #     return redirect('')

        # if not username.isalnum():
        #     messages.error(request,'The username should only contain alpahnumerics')
        #     return redirect('signup/')



        

        myUser=User.objects.create_user(username,password,email)
        

        myUser.save()

        # messages.success(request,'Your Account has been created successfully')
        return redirect('signin')

    return render(request,'core/signup.html')

# new signin view
def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pswrd']

        user=authenticate(username=username,password=password)
        fname=username

        if user is not None:
            login(request,user)
            return render(request,'core/landing.html',{'fname':fname})
        else:
            messages.error(request,'Wrong Username or Password')
            return render(request,'core/landing.html',{'fname':fname})

    return render(request,'core/signin.html')







# def login_view(request):
#     if request.method  == 'POST':        
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user =  authenticate(request, email=email, password=password)
        
#         if user.is_authenticated:
#             return redirect('/landing.html')

#         if user is None:
#             context = {"error": "Invalid email or password"}
#             return render(request, 'core/login.html', context)
#         login(request,user)
#         return redirect('/')
#     return render(request, 'core/signin.html', {})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    return render(request, 'core/logout.html', {})


# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save() 
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password1']
#             user = authenticate(email = email, password=password)
#             login(request, user)
#             messages.success(request, ("Registration Successful"))
#             return redirect('signin/')
#     else:
#         form = UserCreationForm()
#     return render(request, 'core/signup.html', {'form':form})





def faq(request):
    return render(request, "core/faq.html")

def pricing(request):
    return render(request, "core/pricing.html")

def index(request):
    return render(request, "core/index.html")

def dashboard(request):
    return render(request, "core/landing.html")

@login_required
def dashboard_view(request):
    content = render_to_string('createform.html', context=None)
    return HttpResponse(content)