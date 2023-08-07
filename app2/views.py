from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def link1(request):
    return render(request,'new.html')
def link2(request):
    return render(request,'link2.html')
def login(request):
    return render(request,'login.html')
def userprofile(request):
    return render(request,'userprofile.html')