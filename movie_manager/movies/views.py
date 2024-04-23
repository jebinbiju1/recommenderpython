from django.shortcuts import render,redirect
from . models import MovieInfo,Category
from . forms import MovieForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django .contrib.auth import authenticate,login as authlogin,logout as authlogout

def demo(request):
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
    return render(request,'demo.html')

@login_required(login_url='/login/')
def create(request):
    frm=MovieForm()
    if request.POST:
        frm=MovieForm(request.POST,request.FILES)
        if frm.is_valid:
            frm.save()
        return redirect('/')

    return render(request,'create.html',{'frm':frm})

def list(request):
    movie_set=MovieInfo.objects.all()
    print(movie_set)
    return render(request,'list.html',{'movies':movie_set})
@login_required(login_url='/login/')
def edit(request,pk):
    instance_to_be_edited = MovieInfo.objects.get(pk=pk)
    if request.POST:
        frm=MovieForm(request.POST,instance=instance_to_be_edited)
        if frm.is_valid():
            instance_to_be_edited.save()
    else:
        frm = MovieForm(instance=instance_to_be_edited)


    return render(request,'create.html',{'frm':frm})
@login_required(login_url='/login/')
def delete(request,pk):
    instance=MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_set=MovieInfo.objects.all()
    return render(request,'list.html',{'movies':movie_set})
