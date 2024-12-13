from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth,User

def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        # email=request.POST['email']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(userhome)
        else:
            return redirect(userlogin)
    return render(request,'user/userlogin.html')

def adminlogin(request):
    # if request.method=='POST':
    #     username=request.POST['username']
    #     password=request.POST['password']

    return render(request,'admin/adminlogin.html')
def adminhome(request):
    return render(request,'admin/adminhome.html')
def userreg(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        data=User.objects.create_user(username=username,email=email,password=password)
        data.save()
        return redirect(userlogin)
    return render(request,'user/userregister.html')
def userhome(request):
    if '_auth_user_id' in request.session:
        user=User.objects.get(pk=request.session['_auth_user_id'])
        return render(request,'user/userhome.html',{'user':user})
    else:
        return redirect(userlogin)
def userlogout(request):
    if '_auth_user_id' in request.session:
        auth.logout(request)
        return redirect(userlogin)
