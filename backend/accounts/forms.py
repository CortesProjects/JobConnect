from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import StudentProfile, EmployerProfile

User = get_user_model()

class StudentRegistrationForm(UserCreationForm):
   
    email = forms.EmailField(required=True, label="Email Address")
    first_name = forms.CharField(max_length=30, required=True, label="First Name")
    last_name = forms.CharField(max_length=30, required=True, label="Last Name")
    terms_and_conditions = forms.BooleanField(
        required=True, 
        label="I've read and agree with your Terms of Services"
    )
    
    class Meta(UserCreationForm.Meta):
        model = User
       
        fields = (
            'email', 
            'first_name', 
            'last_name'
        )
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if 'username' in self.fields:
             del self.fields['username']

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
    
            if name == 'first_name':
                field.widget.attrs['placeholder'] = 'First Name'
            elif name == 'last_name':
                field.widget.attrs['placeholder'] = 'Last Name'
            elif name == 'email':
                field.widget.attrs['placeholder'] = 'Email address'
            elif name == 'password1':
                field.widget.attrs['placeholder'] = 'Password'
                field.label = False 
            elif name == 'password2':
                field.widget.attrs['placeholder'] = 'Confirm Password'
                field.label = False
           
            if name == 'terms_and_conditions':
                field.widget.attrs.pop('class', None)
                field.label = False
                
    def save(self, commit=True):
        user = super().save(commit=False)
        
        user.user_type = 'student' 
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
            # StudentProfile.objects.create(user=user)
            
        return user


class EmployerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Business Email")
    company_name = forms.CharField(max_length=255, required=True, label="Company Name")
    industry = forms.CharField(max_length=255, required=True, label="Industry")
    terms_and_conditions = forms.BooleanField(
        required=True,
        label="I've read and agree with your Terms of Service"
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'email',
            'company_name',
            'industry'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'username' in self.fields:
            del self.fields['username']  # remove username like student form

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

            if name == 'email':
                field.widget.attrs['placeholder'] = 'Business Email'
            elif name == 'company_name':
                field.widget.attrs['placeholder'] = 'Company Name'
            elif name == 'industry':
                field.widget.attrs['placeholder'] = 'Industry'
            elif name == 'password1':
                field.widget.attrs['placeholder'] = 'Password'
                field.label = False
            elif name == 'password2':
                field.widget.attrs['placeholder'] = 'Confirm Password'
                field.label = False

            if name == 'terms_and_conditions':
                field.widget.attrs.pop('class', None)
                field.label = False

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'employer'
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            EmployerProfile.objects.create(user=user)
        return user