from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

# Best practice is to have a separate urls.py file for each app and then connect it to the main urls.py file of the project

# Adding a namespace to the myapp's url file so that no conflicts happen in the project between apps
app_name = "myapp"


urlpatterns = [
    # URL patterns of API
    path("items-json/", views.item_list_json, name="item_list_json"),
    # URL patterns of API built with DRF
    path("items-api/", views.item_list_api, name="item_list_api"),
    #
    # URL patterns of django app
    ## URL level caching which is the same as view caching
    # path("", cache_page(60 * 15)(views.index), name="index"),
    path("", views.index, name="index"),
    ## Catching id value from the dynamic url
    path("<int:id>/", views.detail, name="detail"),
    path("add/", views.create_item, name="create_item"),
    path("update/<int:pk>/", views.ItemUpdateView.as_view(), name="update_item"),
    path("delete/<int:id>/", views.delete_item, name="delete_item"),
]
