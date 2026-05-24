from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

# HTTP response can return html as well
def item(request):
    return HttpResponse("<h1>This is an item view</h1>")