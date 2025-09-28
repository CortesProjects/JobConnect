from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmployerRegistrationForm
from django.contrib.auth.views import LoginView

def employer_register(request):
    if request.method == 'POST':
        form = EmployerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! Your account is pending verification.')
            return redirect('login')  # or wherever your login page is
    else:
        form = EmployerRegistrationForm()
    return render(request, 'employers/register.html', {'form': form})

class EmployerLoginView(LoginView):
    template_name = 'employers/login.html'
