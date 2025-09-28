from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import StudentRegistrationForm
# from .forms import EmployerRegistrationForm 

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
