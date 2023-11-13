from django.urls import path 

from . import views

app_name="tasks" #to distinguish it from other apps i made when referencing 
urlpatterns=[
   path("", views.index, name='index'),
   path("add", views.add, name='add')
]