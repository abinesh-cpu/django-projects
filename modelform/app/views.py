from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import HttpResponse   

# Create your views here.
def model_form_dis(request):
    data=model_form()
    if request.method=='POST':
        form=model_form(request.POST)
        form.save()
        return redirect(model_form_dis)
    return render(request,'modelforms.html',{'data':data})

# def media_dis(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         email=request.POST['email']
#         return redirect(media_dis)
#     return render(request,'media.html')

def upload_file(request):  
    if request.method == 'POST':  
        filename=request.FILES['file']
        des=request.POST['des']
        data=files.objects.create(file=filename,description=des)
        data.save()
        return redirect(upload_file)
    return render(request,'media.html')