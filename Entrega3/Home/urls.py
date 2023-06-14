from django.urls import path
from Home.views import Home 



urlpatterns = [
    path('', Home, name='home'),
    path('index/', Home, name='home'),
]