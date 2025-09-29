from django.urls import path
from . import views
from .views import employer_register, employer_login

app_name = 'accounts'

urlpatterns = [
    path('registration/', views.student_register, name='register'),
    # path('login/', views.LoginView.as_view(), name='login'),
    path('employer/register/', employer_register, name='employer_register'),
    path('employer/login/', employer_login, name='employer_login'),
]
