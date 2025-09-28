from django import forms
from django.contrib.auth import get_user_model
from .models import EmployerProfile

User = get_user_model()

class EmployerRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    company_name = forms.CharField(max_length=255)
    industry = forms.CharField(max_length=255)
    contact_details = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.role = 'employer'
        if commit:
            user.save()
            EmployerProfile.objects.create(
                user=user,
                company_name=self.cleaned_data['company_name'],
                industry=self.cleaned_data['industry'],
                contact_details=self.cleaned_data['contact_details']
            )
        return user