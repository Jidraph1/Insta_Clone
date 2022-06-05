from django.urls import path
from . import views

#urlPatterns
urlpatterns = [
    path('', views.index, name = 'index'),
    path('post/', views.post, name = 'post')
]