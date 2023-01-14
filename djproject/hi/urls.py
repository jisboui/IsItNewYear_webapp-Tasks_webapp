from django.urls import path
from . import views
urlpatterns =[
    path("",views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("brian", views.brian, name="brian"),
    path("david", views.david, name="david")
    #the two lines above don't have an effect anymore because of me adding line 5 which "overworks" them lets say, but they would work if line 5 deleted i must mention
]