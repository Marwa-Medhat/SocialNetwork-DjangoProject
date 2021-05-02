
from django.urls import path
from . import views


urlpatterns = [
      path("",views.index,name='index'),
      path("create",views.create,name='create'),
      path('delete/<int:id>', views.destroy, name='delete'),  
      path("edit/<int:id>",views.edit, name='edit'), 
]
