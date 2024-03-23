from django import forms
from AppTwo import models

class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = "__all__"
    
