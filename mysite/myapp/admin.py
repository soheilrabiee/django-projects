from django.contrib import admin

from .models import Item

# Register your models here.
# For the admin to have access to it
admin.site.register(Item)
