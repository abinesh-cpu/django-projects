from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def product(request,data,data1):
    return HttpResponse(('product='+str(data*data1))+('<br>sum='+str(data+data1)))