from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer_profile')
    company_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    contact_details = models.TextField()

    def __str__(self):
        return self.company_name
