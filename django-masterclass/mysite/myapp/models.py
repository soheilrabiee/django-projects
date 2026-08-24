from django.db import models
from django.urls import reverse


# Create your models here.
class Item(models.Model):
    # How each object which is a table row represents itself in objects.all() method
    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("myapp:index")

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField()
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500, default="https://alcaratello.com/wp-content/uploads/2021/03/meal-placeholder.jpg"
    )
