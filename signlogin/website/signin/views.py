from django.shortcuts import render
from .forms import bike
# Create your views here.
def demo(request):
    form=bike(request.POST)
    if form.is_valid():
        form.save()
    return render(request,'signup_page.html')    
    