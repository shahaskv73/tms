from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request,'hotel/dashboard.html')

def master(request):
    return render(request,'hotel/master.html')

def add_hotel(request):
    return render(request,'hotel/add_hotel.html')    

def view_hotel(request):
    return render(request,'hotel/view_hotel.html')   

def add_rooms(request):
    return render(request,'hotel/add_rooms.html') 

def view_rooms(request):
    return render(request,'hotel/view_rooms.html')
    
def bookings(request):
    return render(request,'hotel/bookings.html')     

def payments(request):
    return render(request,'hotel/payments.html')               
