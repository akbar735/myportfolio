from django.urls import path
from portfolio import views


urlpatterns = [
     path('', views.Home, name='home'),
     path('skills/', views.Skills, name='skills'),
     path('projects/', views.Projects, name='projects'),
     path('experience/', views.Experience, name='experience'),
     path('others/', views.Others, name='others'),
     path('contact/', views.Contact, name='contact'),
] 