from django.http import HttpResponse
from django.shortcuts import render

from .models import Item


# Create your views here.
def index(request):
    # Model.Manager.Method => how to retrieve data from the database
    item_list = Item.objects.all()

    # Context dict for the render method
    context = {"item_list": item_list}

    # return HttpResponse(item_list)

    # Passing the context object to the render method along with the template
    return render(request, "myapp/index.html", context)


def detail(request, id):
    return HttpResponse(f"This is a detail view for id number {id}")


# HTTP response can return html as well
def item(request):
    return HttpResponse("<h1>This is an item view</h1>")
