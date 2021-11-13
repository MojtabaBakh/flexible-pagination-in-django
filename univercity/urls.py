
from django.contrib import admin
from django.urls import path , include
from .views  import paginationview

urlpatterns = [
 
    path('index/', paginationview ),

    
]
