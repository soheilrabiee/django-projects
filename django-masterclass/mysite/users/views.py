from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect, render

from .forms import RegisterForm

# Create your views here.


def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            # Cleaned data is the data after validation
            username = form.cleaned_data.get("username")
            # Save a success message for the given request
            # The message survives the redirect
            messages.success(request, f"Welcome {username}, your account has been successfully created")
            return redirect("users:login")

    return render(request, "users/register.html", {"form": form})


# Logout needs to be a POST request so we can't use it the same way as the login
def logout_view(request):
    logout(request)
    return render(request, "users/logout.html")


def profile(request):
    return render(request, "users/profile.html")
