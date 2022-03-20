from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request,'index/index.html')

def login(request):
    return render(request,'index/login.html')    

def signup(request):
    return render(request,'index/signup.html')

def tours(request):
    return render(request,'index/tours.html')
  
def contact(request):
    return render(request,'index/contact.html')

def about(request):
    return render(request,'index/about.html')  

def forget_password(request):
    return render(request,'index/forget_password.html')      