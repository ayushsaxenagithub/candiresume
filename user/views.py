from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib import messages
from .forms import ProfileForm

# Create your views here.
def profile(request):
    user = Profile.objects.all()
    context ={'user': user}
    return render(request,'user/profiles.html',context)

def loginUser(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User not found')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'Username or password is incorrect')
    return render(request,'user/login_register.html',)

def logoutUser(request):
    logout(request)
    messages.error(request,'Username successfully logout')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request,'User created successfully')
            login(request,user)
            return redirect('home')

    else:
        messages.success(request,'An error occurred')
    context={'page': page, 'form': form}
    return render(request,'user/login_register.html',context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    name = profile.user.username
    print(name)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context ={'form' : form}
    return render(request,'user/profile_form.html',context)