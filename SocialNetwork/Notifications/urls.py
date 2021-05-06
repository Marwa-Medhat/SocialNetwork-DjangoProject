from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.index, name='notification'),
   
]