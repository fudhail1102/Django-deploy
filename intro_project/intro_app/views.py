from django.shortcuts import render
from django.http import HttpResponse
from intro_app.models import WebPage,Topic,AccessRecord
from intro_app import forms

# Create your views here.

def index(request):
    webpages = AccessRecord.objects.order_by("date")
    template_tags = {"template_tag":"I am django template tag","access_records":webpages}
    return render(request,"intro_app/index.html",context=template_tags)

def webpage_form(request):
    form = forms.Webpage()
    if request.method == 'POST':
        form = forms.Webpage(request.POST)
        if form.is_valid():
            print("Form Validated")
            print(form.cleaned_data["topic"])
            print(form.cleaned_data["name"])
            print(form.cleaned_data["link"])
            print("Data Received")

    return render(request,"intro_app/forms.html",context={"form":form})
