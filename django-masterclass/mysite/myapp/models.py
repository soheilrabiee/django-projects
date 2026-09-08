from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from .managers import ItemManager


# Create your models here.
class Item(models.Model):
    class Meta:
        # Create a composite index which includes the user_name and the item_price fields
        indexes = [
            models.Index(fields=["user_name", "item_price"]),
        ]

    # How each object which is a table row represents itself in objects.all() method
    def __str__(self):
        return self.item_name + " : " + str(self.item_price)

    def get_absolute_url(self):
        return reverse("myapp:index")

    # Django automatically adds "_id" to the database column of a ForeignKey, while the model field keeps its original name.
    # Both user_name and user_name_id can be used by django. The first on points to the object and the second one to the actual value of the database for that field
    # db_column can be used to change this behavior by specifying the name for the database
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200, db_index=True)
    item_desc = models.CharField()
    item_price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    item_image = models.URLField(
        max_length=500, default="https://alcaratello.com/wp-content/uploads/2021/03/meal-placeholder.jpg"
    )
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Connecting the custom manager to the model
    objects = ItemManager()


class Category(models.Model):
    name = models.CharField(max_length=100)
    added_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
