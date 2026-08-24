from django.urls import path

from . import views

# Best practice is to have a separate urls.py file for each app and then connect it to the main urls.py file of the project

# Adding a namespace to the myapp's url file so that no conflicts happen in the project between apps
app_name = "myapp"


urlpatterns = [
    path("", views.index, name="index"),
    # Catching id value from the dynamic url
    path("<int:id>/", views.detail, name="detail"),
    path("add/", views.ItemCreateView.as_view(), name="create_item"),
    path("update/<int:id>/", views.update_item, name="update_item"),
    path("delete/<int:id>/", views.delete_item, name="delete_item"),
]
