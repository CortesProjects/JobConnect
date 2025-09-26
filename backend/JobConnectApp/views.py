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
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        supabase.table("users").insert({
            "username": username,
            "email": email,
            "password": password
        }).execute()

        return HttpResponse("Registration successful!")
    return render(request, "authentication_page/register.html")


def home(request):
    user = request.session.get("admins")  # None if not logged in
    return render(request, "home.html", {"admins": user})



def logout_view(request):
    request.session.flush()  # clears all session data
    return redirect("admin_login")
