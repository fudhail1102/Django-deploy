from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo import forms

# Create your views here.

def index(request):
    return render(request,"AppTwo/index.html")

def help(request):
    help_dict = {"help_tag":"Help Page!"}
    return render(request,"AppTwo/help.html",context=help_dict)

def users(request):
    user_dets = User.objects.order_by("first_name")
    user_dict ={"user_details":user_dets}
    return render(request,"AppTwo/user.html",context=user_dict)

def signup(request):
    user_form = forms.UserForm()

    if request.method =='POST':
        user_form = forms.UserForm(request.POST)

        if user_form.is_valid():
            user_form.save(commit=True)
            return users(request)

    return render(request,"AppTwo/signup.html",context={"form":user_form})