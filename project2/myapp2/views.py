from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth,User

def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        data=User.objects.create_user(username=username,email=email,password=password)
    return render(request,'user/userlogin.html')

def adminlogin(request):
    # if request.method=='POST':
    #     username=request.POST['username']
    #     password=request.POST['password']

    return render(request,'admin/adminlogin.html')
def adminhome(request):
    return render(request,'admin/adminhome.html')
def userreg(request):
    # if request.method=='POST':
    #     slno=len(users)
    #     username=request.POST['username']
    #     password=request.POST['password']
    #     email=request.POST['email']
    #     return redirect(userlogin)
    return render(request,'user/userregister.html')
def userhome(request):
    # if request.method=='POST':
    #     username=request.POST['username']
    #     password=request.POST['password']
    #     email=request.POST['email']
    return render(request,'user/userhome.html')