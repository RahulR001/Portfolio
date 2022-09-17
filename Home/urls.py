from django.urls import path
from Home import views


# ========== portfolio-app-url-patterns ==========

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('Projects', views.Projects, name='Projects'),
     
]
