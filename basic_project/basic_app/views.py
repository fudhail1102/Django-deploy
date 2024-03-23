from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from basic_app.forms import UserForm, UserProfileForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request):
    return render(request,"basic_app/index.html")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("User not active")
        
        else:
            return HttpResponse("Invalid Login Details")
    else:
        return render(request,"basic_app/login.html",context={})


def register(request):
    registered = False

    user_form = UserForm()
    profile_form = UserProfileForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    
    return render(request,"basic_app/register.html",context={"registered":registered,"user_form":user_form,"profile_form":profile_form})