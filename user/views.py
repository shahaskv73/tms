from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'user/index.html')

def master(request):
    return render(request,'user/master.html')    