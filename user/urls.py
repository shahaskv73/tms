from django.urls import path
from .import views 
urlpatterns=[
    
    path('dashboard1/',views.dashboard1),
    path('master1/',views.master1),

]