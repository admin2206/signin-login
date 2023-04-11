from django import forms
from .models import signcar
class signbike(forms.ModelForm):
    class Meta:
        model=signcar
        fields=["email","password"]