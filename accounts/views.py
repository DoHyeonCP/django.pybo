from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from accounts.forms import UserForm
from .models import Profile
from .forms import ProfileForm
from pybo.models import Question


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(username=user)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})

def user_profile(request, username):
    user = User.objects.get(username = username)
    profile = Profile.objects.get(username = user)
    questions = Question.objects.filter(author=user)

    if request.method == "POST":
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
    else:
        form = ProfileForm(instance=profile)

    context = {
        'user': user,
        'profile': profile,
        'questions': questions,
        'form': form,
    }
    return render(request, 'accounts/user_profile.html', context)