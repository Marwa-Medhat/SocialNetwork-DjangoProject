from django.urls import path

from . import views

urlpatterns = [
    path('register', views.registration_view, name='register'),
    path('profile', views.profile, name='profile'),
    path('profile/<int:id>', views.userprofile, name='userprofile'),
    path('request/<int:id>', views.friendRequest, name='friendRequest'),
    path('list', views.index, name='listusers'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login'),
    path("editprofile/<int:id>", views.editprofile, name="editprofile"),
    # path("editprofile", views.editprofile, name="editprofile"),



]
