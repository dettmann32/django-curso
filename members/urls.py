from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('',views.home,name="home"),
    path('allmembers/', views.allmembers, name='allmembers'),
    path('allmembers/details/<int:id>',views.details,name='details'),
    path('testing/', views.fruits, name='testing')
   
]