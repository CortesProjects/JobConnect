#MyApp/urls.py
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='homepage.html'), name='homepage'),
    path('admin_login/', views.admin_site, name='admin_login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path("logout/", views.logout_view, name="logout")
]