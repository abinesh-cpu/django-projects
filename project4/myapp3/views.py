from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
users=[]
def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        users.append({'username':username,'password':password})
        return redirect(userhome)
    return render(request,'userlogin.html',{'users':users})
adminusername="abi123"
adminpassword="abi@123"
def adminlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if username==adminusername and password==adminpassword:
            print("logged in")
            return redirect(adminhome)
    return render(request,'adminlogin.html')
def adminhome(request):
    return render(request,'adminhome.html')
def userreg(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        return redirect(userlogin)
    return render(request,'userregister.html')
def userhome(request):
    return render(request,'userhome.html')