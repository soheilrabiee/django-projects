from django.urls import path
from . import views

# Best practice is to have a separate urls.py file for each app and then connect it to the main urls.py file of the project

urlpatterns = [
    path('',views.index),
]
