from django.urls import path
from . import views

urlpatterns = [
   # path('admin/', admin.site.urls),
   path('', views.hello , name = "Hello"),
   path('service' , views.service , name = "Service Page"),
   path('niradhar' , views.niradhar , name = "Niradhar Page")
]
