from django.shortcuts import render,redirect

# Create your views here.
users=[]
def index(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        users.append({'username':username,'password':password})
        return redirect(adminlogin)
    return render(request,'index.html')
def adminlogin(request):
    return render(request,'admin_login.html')