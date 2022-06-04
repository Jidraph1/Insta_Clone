from django.urls import path
from . import views

#urlPatterns
urlpatterns = [
    path('', views.index, name = 'index')
]