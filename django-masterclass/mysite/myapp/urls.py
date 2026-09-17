from django.urls import include, path
from django.views.decorators.cache import cache_page
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

# Best practice is to have a separate urls.py file for each app and then connect it to the main urls.py file of the project

# Adding a namespace to the myapp's url file so that no conflicts happen in the project between apps
app_name = "myapp"


router = DefaultRouter()
# Basename is used for url names and is useful when using functions like reverse to generate a url
router.register(r"items", views.ItemViewSet, basename="item")

urlpatterns = [
    # JWT token url patterns
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    #
    # Creates the whole CRUD operation routes
    path("api/", include(router.urls)),
    #
    # # URL patterns of API built with DRF
    # path("api/items/", views.ItemListCreateAPI.as_view(), name="item_list_api"),
    # # URL pattern for single item
    # path("api/items/<int:pk>", views.ItemRetrieveUpdateDestroyAPIView.as_view(), name="item_detail_api"),
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
