from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
users=[]
def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        for i in users:
            if i['username']==username and i['password']==password and i['email']==email:
                print("logged in successfully")
        # users.append({'username':username,'password':password})
                return redirect(userhome)
    return render(request,'index.html')
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
    return render(request,'adminhome.html',{'users':users})
def userreg(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        users.append({'username':username,'password':password,'email':email})
        return redirect(userlogin)
    return render(request,'userregister.html')
def userhome(request):
    return render(request,'userhome.html')