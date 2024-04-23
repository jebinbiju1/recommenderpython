from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django .contrib.auth import authenticate,login as authlogin,logout as authlogout


def login(request):
    error_message=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            authlogin(request,user)
            return redirect('list')
        else:
            error_message='invalid credentials'

    return render(request,'users/login.html',{'error_message':error_message})

def logout(request):
    authlogout(request)
    return redirect('login')

def signup(request):
    if request.method =='POST':
        name=request.POST['name']
        names=request.POST['names']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            return redirect('users/login.html')
        else:
            user=User.objects.create_user(first_name=name,last_name=names,username=username,email=email,password=password)


    return render(request,'users/create.html')

def profile(request):
    return render(request,'users/profile.html')

def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['name']
        user.last_name = request.POST['names']
        user.username= request.POST['username']
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.save()

    return render(request, 'users/edit_profile.html',{'user':request.user})

