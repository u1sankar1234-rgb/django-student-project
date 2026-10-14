from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('servies/', views.services, name='servies'),  # alias for backwards compatibility
    path('contact/', views.contact, name='contact'),
    path('form/', views.form_view, name='form'),
]