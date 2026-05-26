from django.db import models


# Create your models here.
class Item(models.Model):
    # How each object which is a table row represents itself in objects.all() method
    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField()
    item_price = models.IntegerField()
