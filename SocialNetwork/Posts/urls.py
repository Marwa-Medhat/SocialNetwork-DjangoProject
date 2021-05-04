
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.index, name='index'),
    path("details/<int:id>", views.details, name='details'),
    path("create", views.create, name='create'),
    path('delete/<int:id>', views.destroy, name='delete'),
    path("edit/<int:id>", views.edit, name='edit'),
    path('like', views.like_post, name='like_post'),
    path('mustauth', views.must_authenticate_view, name="mustauth"),
    path('comment/<int:id>', views.comment, name='comment'),

]
