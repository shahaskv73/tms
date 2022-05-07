from django.urls import path
from .import views 
urlpatterns=[
    
    path('dashboard/',views.dashboard,name="dashboard"),
    path('master/',views.master),
    path('add_hotel/',views.add_hotel,name="add_hotel"),
    path('add_rooms/',views.add_rooms,name="add_rooms"),
    path('view_hotels/',views.view_hotel,name="view_hotel"),
    path('view_rooms/',views.view_rooms,name="view_rooms"),
    path('bookings/',views.bookings,name="bookings"),
    path('payments/',views.payments,name="payments"),

]