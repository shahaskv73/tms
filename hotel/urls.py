from django.urls import path
from .import views 
urlpatterns=[
    
    path('dashboard/',views.dashboard),
    path('master/',views.master),

]