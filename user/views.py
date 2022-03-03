from django.shortcuts import render

# Create your views here.
def dashboard1(request):
    return render(request,'dashboard1.html')

def master1(request):
    return render(request,'master1.html')    