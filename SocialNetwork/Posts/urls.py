
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
      path("",views.index,name='index'),
      path("create",views.create,name='create'),
      path('delete/<int:id>', views.destroy, name='delete'),  
      path("edit/<int:id>",views.edit, name='edit'), 
      path('like/<int:pk>',views.like,name='like_post')
]
