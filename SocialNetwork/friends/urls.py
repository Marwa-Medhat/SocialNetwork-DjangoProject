
from django.urls import path
from . import views

urlpatterns = [
    path('request/', views.send_friend_request, name='friendRequest'),
   
]