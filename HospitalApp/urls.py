from django.contrib import admin
from django.urls import path
from HospitalApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('starter/', views.starter, name='starter-page'),
    path('service/', views.service, name='service-details'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('departments/', views.departments, name='departments'),

    path('doctors/', views.doctors, name='doctors'),
    path('appointment/', views.appoint, name='appointment'),
    path('contact/', views.contacts, name='contact'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete, name='show'),





]
