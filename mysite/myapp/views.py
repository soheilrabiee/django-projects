from django.http import HttpResponse
from django.shortcuts import render

from .models import Item


# Create your views here.
def index(request):
    # Model.Manager.Method => how to retrieve data from the database
    item_list = Item.objects.all()

    # return HttpResponse(item_list)

    # Render a template for index view
    return render(request, "myapp/index.html")


# HTTP response can return html as well
def item(request):
    return HttpResponse("<h1>This is an item view</h1>")
