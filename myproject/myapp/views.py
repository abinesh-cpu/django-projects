from django.shortcuts import render,redirect
# from django.http import HttpResponse
from .models import *

# Create your views here.
adminusername="abi123"
adminpassword="abi@123"
def adminlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if username==adminusername and password==adminpassword:
            print("logged in")
            request.session['adm']=adminusername
            return redirect(adminhome)
    return render(request,'adminlogin.html')
def adminhome(request):
    return render(request,'adminhome.html')
def employereg(request):
    return render(request,'emp-reg.html')