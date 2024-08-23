from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('saludos/', views.presentacion),

]
