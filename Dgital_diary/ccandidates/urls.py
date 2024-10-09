from django.urls import path
from . import views

urlpatterns = [
   path('', views.hello , name = "Hello"),
   path('service' , views.service , name = "Service Page"),
   path('niradhar' , views.Niradhar , name = "Niradhar Page")
]
