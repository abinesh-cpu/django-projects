from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
    return render(request,'index.html')