# Django has a built-in view ready to use for login
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    # The as_view method needs to be called whenever a class based view is used
    path("login/", auth_views.LoginView.as_view(), name="login"),
]
