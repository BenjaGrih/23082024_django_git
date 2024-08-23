from django.urls import path
from . import views

urlpatterns = [
    path('jaja/', views.jaja),
    path('matanga/', views.matanga),
    path('', views.index),

]
