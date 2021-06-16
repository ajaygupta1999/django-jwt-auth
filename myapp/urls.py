from django.urls import path, include
from myapp import views


urlpatterns = [
    path("" , views.home),
    path('verify/data' , views.decodedata)
]
