from django.urls import path
from .views import employer_register, EmployerLoginView

urlpatterns = [
    path('register/', employer_register, name='employer_register'),
    path('login/', EmployerLoginView.as_view(), name='employer_login'),
]