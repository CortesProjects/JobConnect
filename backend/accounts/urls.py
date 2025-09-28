from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('registration/', views.student_register, name='register'),
    # path('login/', views.LoginView.as_view(), name='login'),
]
