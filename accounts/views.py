from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from . forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required,permission_required

def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"User has been Succefully")
            return redirect('accounts:login_page')
    else:
        form=RegisterForm()
    return render(request,'accounts/register.html',{'form':form})

def login_page(request):
    if request.method=="POST":
        form=AuthenticationForm(request,request.POST)

        if form.is_valid():

            user=form.get_user()

            auth.login(request,user)

            messages.success(request,'You Have Login Succefully')

            return redirect('dashboard:dashboard')
        messages.error(request,"Inavlid Username or Password")
    else:
        form=AuthenticationForm()

    return render(request,"accounts/login_page.html",{"form":form})

def logout_page(request):
    auth.logout(request)
    return redirect('myapp:home')