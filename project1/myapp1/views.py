from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request,data):
    return render(request,'index.html',{'data':data})
def index1(request):
    return render(request,'index1.html')