from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request,'adm/dashboard.html')

def master(request):
    return render(request,'adm/master.html') 

def user_info(request):
    return render(request,'adm/user_info.html')    

def hotel_approval(request):
    return render(request,'adm/hotel_approval.html') 

def manage_trips(request):
    return render(request,'adm/manage_trips.html')           

 

    
