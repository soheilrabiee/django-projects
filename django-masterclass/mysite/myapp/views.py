# from django.http import HttpResponse
import logging

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import ItemForm
from .models import Item
from .permissions import IsOwnerOrReadOnly
from .serializers import ItemSerializer

# Shows the module in which the logger has created the logs
logger = logging.getLogger(__name__)


# Viewset handles the whole CRUD operations with actions
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["item_name", "item_price"]
    ordering_fields = ["item_name", "item_price"]

    # Saves the user inside the user_name field whenever we want to create an item
    def perform_create(self, serializer):
        return serializer.save(user_name=self.request.user)


# # Generic View for list/create items
# class ItemListCreateAPI(generics.ListCreateAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer


# # Generic View for Retrieve/update/delete item details
# class ItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     # Base queryset. DRF uses the URL's pk to retrieve the specific object
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer


# # Class based view without using generics
# class ItemListAPIView(APIView):
#     def get(self, request):
#         items = Item.objects.all()
#         serializer = ItemSerializer(items, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


## Allow this view to handle GET requests
# @api_view(["GET", "POST"])
# def item_list_api(request):

#     # Read functionality
#     if request.method == "GET":
#         items = Item.objects.all()
#         # Serialize multiple Item objects
#         serializer = ItemSerializer(items, many=True)
#         # Return the serialized data as an API response
#         return Response(serializer.data)

#     # Create functionality
#     elif request.method == "POST":
#         # The exact opposite steps of the GET request
#         serializer = ItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


# # Class based view without using generics
# class ItemDetailAPIView(APIView):
#     # Custom method to get a specific item
#     def get_object(self, pk):
#         try:
#             return Item.objects.get(pk=pk)
#         except Item.DoesNotExist:
#             return None

#     def get(self, request, pk):
#         item = self.get_object(pk)
#         if not item:
#             return Response({"Error": "Item not found"})
#         serializer = ItemSerializer(item)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         item = self.get_object(pk)
#         if not item:
#             return Response({"Error": "Item not found"})
#         serializer = ItemSerializer(item, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#     def delete(self, request, pk):
#         item = self.get_object(pk)
#         if not item:
#             return Response({"Error": "Item not found"})
#         item.delete()
#         return Response({"message": "Item deleted"})


# @api_view(["GET", "PUT", "DELETE"])
# def item_detail_api(request, pk):
#     item = Item.objects.get(pk=pk)

#     # Read functionality
#     if request.method == "GET":
#         serializer = ItemSerializer(item)
#         return Response(serializer.data)

#     # Update functionality
#     elif request.method == "PUT":
#         serializer = ItemSerializer(item, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#     # Delete functionality
#     elif request.method == "DELETE":
#         item.delete()
#         return Response({"message": "Item deleted"})


# This view can't be used if the user is not logged in
@login_required
## Number of seconds that the cache is valid
# @cache_page(60 * 15)
# @vary_on_headers("User-Agent")
def index(request):
    logger.info("Fetching all items from the database")
    # Log time, user and ip address of the request
    logger.info(
        "User %s [%s] requested item list from %s",
        request.user,
        timezone.now().isoformat(),
        request.META.get("REMOTE_ADDR"),
    )

    # Model.Manager.Method => how to retrieve data from the database
    item_list = Item.objects.all()

    # Better to use placeholders rather than f-strings for messages
    logger.debug("Found %s items", item_list.count())

    paginator = Paginator(item_list, 5)
    # Get the url parameter through the request
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Context dict for the render method
    context = {"page_obj": page_obj}

    # Passing the context object to the render method along with the template
    return render(request, "myapp/index.html", context)


## Generic listView that retrieves all Item objects and passes them to the template as "item_list"

# class IndexClassView(ListView):
#     model = Item
#     template_name = "myapp/index.html"
#     context_object_name = "item_list"


def detail(request, id):
    logger.info("Fetching an item with id: %s", id)

    # Use get_object_or_404 to handle the object not found for the detail view
    item = get_object_or_404(Item, pk=id)
    logger.debug("Item found %s ($%s)", item.item_name, item.item_price)

    ## Log the exception with its traceback and re-raise it for higher-level handling
    # try:
    #     item = Item.objects.get(id=id)
    #     logger.debug("Item found %s ($%s)", item.item_name, item.item_price)
    # except Exception:
    #     logger.exception("Error fetching the item with id %s : %s", id)
    #     raise

    context = {"item": item}

    # return HttpResponse(f"This is a detail view for id number {item}")

    return render(request, "myapp/detail.html", context)


## Generic detailView retrieves one Item using its primary key (pk) from the URL

# class FoodDetail(DetailView):
#     model = Item
#     template_name = "myapp/detail.html"
#     context_object_name = "item"


# HTTP response can return html as well
# def item(request):
#     return HttpResponse("<h1>This is an item view</h1>")


def create_item(request):
    # Instead of having two instances of the form object for GET and POST methods
    form = ItemForm(request.POST or None)

    if request.method == "POST":
        # form = ItemForm(request.POST)
        if form.is_valid():
            # Save the content to the database
            form.save()
            return redirect("myapp:index")

    ## Views are automatically programmed to handle GET requests so it doesn't need a condition for it
    ## Create an instance of the form class
    # form = ItemForm()
    context = {"form": form}
    return render(request, "myapp/item-form.html", context)


## CreateView generates a form for the specified Item fields and saves the submitted data as a new Item
## Django automatically uses "modelname_form.html" for template
## Redirecting is needed after the submission using get_absolute_url
class ItemCreateView(CreateView):
    model = Item
    fields = ["item_name", "item_desc", "item_price", "item_image"]

    # This method is used to add logic before the form is saved
    def form_valid(self, form):
        # Add the user_name to the form data
        form.instance.user_name = self.request.user

        # Continue with the django form_valid method and return its value
        return super().form_valid(form)


def update_item(request, id):
    item = Item.objects.get(id=id)
    # Prepopulate the form with the item values
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("myapp:index")
    return render(request, "myapp/item-form.html", {"form": form})


class ItemUpdateView(UpdateView):
    model = Item
    fields = ["item_name", "item_desc", "item_price", "item_image"]
    # Changes the suffix of the template from "modelname_form.html"
    template_name_suffix = "_update_form"

    # Restricts the queryset to items owned by the currently logged-in user
    def get_queryset(self):
        return Item.objects.filter(user_name=self.request.user)


def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect("myapp:index")
    return render(request, "myapp/item-delete.html")


class ItemDelete(DeleteView):
    model = Item
    # The item instance will be deleted so the get_absolute_url method cannot be used to redirect the user
    success_url = reverse_lazy("myapp:index")
