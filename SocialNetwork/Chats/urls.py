from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='chat'),
    path('<str:user_id>/', views.room, name='chatroom'),
    path('<str:user_id>/', views.room, name='chatroom'),
]