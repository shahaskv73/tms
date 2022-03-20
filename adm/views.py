from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request,'adm/dashboard.html')

def master(request):
    return render(request,'adm/master.html')     

 

    
