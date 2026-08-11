# Django automatically handles the user creation form and model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

# Create your views here.


def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("myapp:index")

    return render(request, "users/register.html", {"form": form})
