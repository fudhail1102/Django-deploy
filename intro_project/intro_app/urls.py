from django.urls import path
from intro_app import views

app_name = "intro_app"

urlpatterns = [
    path(r"",views.index,name='index'),
    path(r'formpage/',views.webpage_form,name="webpage_form"),
]
