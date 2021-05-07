from django.urls import path

from . import views

urlpatterns = [
    path('register', views.registration_view, name='register'),
    path('profile', views.profile, name='profile'),
    path('profile/<int:id>', views.userprofile, name='userprofile'),
    path('list', views.index, name='listusers'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login'),
    path("editprofile/<int:id>", views.editprofile, name="editprofile"),
    path('my-invites/', views.invites_received_view, name='my-invites-view'),
    path('my-invites/acctept/', views.accept_invatation, name='accept-invite'),
    path('my-invites/reject/', views.reject_invatation, name='reject-invite'),
    path('send-invite/', views.send_invatation, name='send-invite'),
    path('friendslist/', views.friendslist, name='friendslist'),

    # path("editprofile", views.editprofile, name="editprofile"),
]
