from django.urls import path
from .import views 
urlpatterns=[
    
    path('',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
     path('hotel_login/',views.hotel_login,name="hotel_login"),
    path('hotel_signup/',views.hotel_signup,name="hotel_signup"),
    path('tours/',views.tours,name="tours"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('forget_password/',views.forget_password,name="forget"),
    
]