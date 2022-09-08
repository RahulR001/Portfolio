from django.urls import path
from Home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('Projects', views.Projects, name='Projects'),
     
]
