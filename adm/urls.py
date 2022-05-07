from django.urls import path
from .import views 
urlpatterns=[
    
    path('dashboard/',views.dashboard,name="dashboard1"),
    path('master/',views.master),
    path('user_info/',views.user_info,name="user_info"),
    path('hotel_approval/',views.hotel_approval,name="hotel_approval"),
    path('manage_trips/',views.manage_trips,name="manage_trips"),

]