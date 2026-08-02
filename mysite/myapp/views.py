# from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ItemForm
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
    item = Item.objects.get(id=id)
    context = {"item": item}

    # return HttpResponse(f"This is a detail view for id number {item}")

    return render(request, "myapp/detail.html", context)


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
        print("Post request is triggered!")

    ## Views are automatically programmed to handle GET requests so it doesn't need a condition for it
    ## Create an instance of the form class
    # form = ItemForm()
    context = {"form": form}
    return render(request, "myapp/item-form.html", context)
