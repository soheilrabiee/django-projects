from django.contrib import messages
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
