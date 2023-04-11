from django import forms
from .models import car
class bike(forms.ModelForm):
    class Meta:
        model=car
        fields=["first_name","last_name","email","password"]