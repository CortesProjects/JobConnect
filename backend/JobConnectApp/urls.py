#MyApp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('admin_login/', views.admin_site, name='admin_login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path("logout/", views.logout_view, name="logout"),
]