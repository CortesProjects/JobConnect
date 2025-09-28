from django.http import HttpResponse
from django.shortcuts import redirect, render
from supabase import create_client
from django.conf import settings

supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)


def admin_site(request):
    context = {}

    if request.method == "POST":
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        context["email_value"] = email  

        response = supabase.table("admins").select("*").eq("email", email).execute()

        if not response.data:
            context["email_error"] = "Email does not exist."
        else:
            user = response.data[0]
            if user["password"] != password:
                context["password_error"] = "Password is incorrect."
            else:
                # ✅ Save user info in session
                request.session["admins"] = {
                    "id": user["id"],
                    "email": user["email"],
                    "username": user.get("username", "")
                }
                return redirect("home")

    return render(request, "authentication_page/admin.html", context)



def register(request):
    context = {}

    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip().lower()  # normalize email
        password = request.POST.get("password", "").strip()
        confirm_password = request.POST.get("confirm_password", "").strip()
        role = request.POST.get("role", "")  # default to applicant

        context.update({
            "full_name_value": full_name,
            "username_value": username,
            "email_value": email,
            "role_value": role
        })

        # Basic validation
        if not all([full_name, username, email, password, confirm_password]):
            context["error"] = "All fields are required."
        elif password != confirm_password:
            context["error"] = "Passwords do not match."
        else:
            # Determine target table
            table_name = "user_employers" if role == "employer" else "user_applicants"

            # ✅ Check for duplicate email across both tables
            email_in_applicants = supabase.table("user_applicants").select("*").eq("email", email).execute()
            email_in_employers = supabase.table("user_employers").select("*").eq("email", email).execute()

            if email_in_applicants.data:
                context["email_error"] = "This email is already registered as an applicant."
            elif email_in_employers.data:
                context["email_error"] = "This email is already registered as an employer."

            # Check if username exists in target table only if email is unique
            if not context.get("email_error"):
                existing_username = supabase.table(table_name).select("*").eq("username", username).execute()
                if existing_username.data:
                    context["username_error"] = "This username is already taken."

            # Insert only if no errors
            if not context.get("email_error") and not context.get("username_error"):
                response = supabase.table(table_name).insert({
                    "full_name": full_name,
                    "username": username,
                    "email": email,
                    "password": password  # ⚠️ hash in production
                }).execute()

                if response.data:
                    request.session[role] = {
                        "id": response.data[0]["id"],
                        "email": email,
                        "username": username
                    }
                    return redirect("login")
                else:
                    context["error"] = "Something went wrong. Please try again."

    return render(request, "authentication_page/register.html", context)



def login_site(request):
    context = {}

    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "").strip()

        context["email_value"] = email

        # Check applicants and employers
        applicant_resp = supabase.table("user_applicants").select("*").eq("email", email).execute()
        employer_resp = supabase.table("user_employers").select("*").eq("email", email).execute()

        user = None
        role = None

        if applicant_resp.data:
            user = applicant_resp.data[0]
            role = "applicant"
        elif employer_resp.data:
            user = employer_resp.data[0]
            role = "employer"

        if not user:
            context["email_error"] = "Email does not exist."
        elif user["password"] != password:
            context["password_error"] = "Password is incorrect."
        else:
            # ⚠️ Clear previous sessions first
            request.session.flush()

            # Save new session
            request.session[role] = {
                "id": user["id"],
                "email": user["email"],
                "username": user["username"]
            }

            return redirect("home")

    return render(request, "authentication_page/login.html", context)


    


def home(request):
    # Check which session exists
    user = None
    role = None

    if request.session.get("admins"):
        user = request.session.get("admins")
        role = "Admin"
    elif request.session.get("applicant"):
        user = request.session.get("applicant")
        role = "Applicant"
    elif request.session.get("employer"):
        user = request.session.get("employer")
        role = "Employer"

    return render(request, "home.html", {"user": user, "role": role})




def logout_view(request):
    request.session.flush()  # clears all session data
    return redirect("admin_login")

def base(request):
    return render(request, "base.html")