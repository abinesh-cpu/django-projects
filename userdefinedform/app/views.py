from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def user_form_dis(request):
    data=user_form
    return render(request,'stud.html',{'data':data})