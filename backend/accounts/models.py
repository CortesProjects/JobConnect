from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('employer', 'Employer'),
    )
    
    user_type = models.CharField(
        max_length=10, 
        choices=USER_TYPE_CHOICES, 
        default='student',
        verbose_name='User Type'
    )
    
    def __str__(self):
        return self.email or self.username

class StudentProfile(models.Model):
    """Placeholder for student-specific data."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
   
    def __str__(self):
        return f"Student Profile for {self.user.email}"

class EmployerProfile(models.Model):
    """Placeholder for employer-specific data."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return f"Employer Profile for {self.user.email}"
