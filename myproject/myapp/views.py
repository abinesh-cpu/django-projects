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
    emps=employee.objects.all()
    deps=department.objects.all()
    if request.method=='POST':
        dep=request.POST['d']
        deppk=department.objects.get(pk=dep)
        emps=employee.objects.filter(dname=deppk)
    return render(request,'adminhome.html',{'deps':deps,'emps':emps})
def employereg(request):
    return render(request,'emp-reg.html')