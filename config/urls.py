from django.urls import path
from portfolio import views

urlpatterns = [path('', views.home, name='home'), path('projects/<slug:slug>/', views.project, name='project'), path('resume/', views.resume, name='resume')]
