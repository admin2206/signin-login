from django.shortcuts import render,HttpResponse,redirect
from .forms import signbike
from django.contrib.auth import authenticate,login
def loginaction(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        login=authenticate(request,email=email,password=password)
        if login is not None:
            form=signbike(request,login)
            return render(request,'welcome.html')    
        else:
            return render(request,'error.html')