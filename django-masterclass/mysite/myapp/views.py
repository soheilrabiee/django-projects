# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import ItemForm
from .models import Item


# This view can't be used if the user is not logged in
@login_required
def index(request):
    # Model.Manager.Method => how to retrieve data from the database
    item_list = Item.objects.all()

    # Context dict for the render method
    context = {"item_list": item_list}

    # return HttpResponse(item_list)

    # Passing the context object to the render method along with the template
    return render(request, "myapp/index.html", context)


## Generic listView that retrieves all Item objects and passes them to the template as "item_list"

# class IndexClassView(ListView):
#     model = Item
#     template_name = "myapp/index.html"
#     context_object_name = "item_list"


def detail(request, id):
    item = Item.objects.get(id=id)
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
        print("Post request is triggered!")

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


def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect("myapp:index")
    return render(request, "myapp/item-delete.html")


class ItemDelete(DeleteView):
    model = Item
