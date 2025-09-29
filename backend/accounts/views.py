from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import StudentRegistrationForm
from .forms import EmployerRegistrationForm
from .models import User


def student_register(request):
  
    if request.user.is_authenticated:
        return redirect('homepage') 

    if request.method == 'POST':
        account_type = request.POST.get('account_type', 'applicant')
        form = StudentRegistrationForm(request.POST)

        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                messages.success(request, f'Registration successful! Welcome to JobConnect as a {account_type.capitalize()}.')
                return redirect('homepage') 
            except IntegrityError as e:
                # Handle database errors (e.g., if a constraint is violated)
                messages.error(request, "A database error occurred during registration. Please try again.")
                # Log the detailed error (if logging is set up)
                print(f"Integrity Error during user save: {e}")
            except Exception as e:
                # Catch any other unexpected errors during save/login
                messages.error(request, "An unexpected error occurred. Please contact support.")
                print(f"Unexpected Error during registration: {e}")
               
        else:
            pass 
            
    else:
        form = StudentRegistrationForm()
        
    context = {
        'form': form
    }
    return render(request, 'accounts/registration.html', context)

def employer_register(request):
    # If user already logged in → redirect
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        account_type = request.POST.get('account_type', 'employer')
        form = EmployerRegistrationForm(request.POST)

        if form.is_valid():
            try:
                user = form.save()  # This sets user_type='employer'
                login(request, user)
                messages.success(
                    request,
                    f'Registration successful! Welcome to JobConnect as an {account_type.capitalize()}.'
                )
                return redirect('homepage')  # or your employer dashboard
            except IntegrityError as e:
                messages.error(
                    request,
                    "A database error occurred during registration. Please try again."
                )
                print(f"Integrity Error during employer save: {e}")
            except Exception as e:
                messages.error(
                    request,
                    "An unexpected error occurred. Please contact support."
                )
                print(f"Unexpected Error during employer registration: {e}")
        # else → form invalid → fall through to re-render with errors
    else:
        form = EmployerRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/employer_registration.html', context)

def employer_login(request):
    """Employer login view."""
    if request.user.is_authenticated:
        # already logged in → redirect to homepage or employer dashboard
        return redirect('homepage')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Since you’re using email as the primary login field
        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username  # get the username (Django uses it internally)
        except User.DoesNotExist:
            username = None

        user = authenticate(request, username=username, password=password)

        if user is not None and user.user_type == 'employer':
            login(request, user)
            messages.success(request, 'Welcome back Employer!')
            return redirect('homepage')  # or employer dashboard
        else:
            messages.error(request, 'Invalid credentials or not an Employer account.')

    return render(request, 'accounts/employer_login.html')