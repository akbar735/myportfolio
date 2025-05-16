from django.urls import path
from portfolio import views


urlpatterns = [
     path('', views.Home, name='home'),
     path('contact/', views.Contact, name='contact'),
] 