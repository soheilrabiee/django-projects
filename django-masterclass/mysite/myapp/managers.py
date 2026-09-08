from django.db import models


class ItemManager(models.Manager):
    def cheap_items(self):
        return self.filter(item_price__lt=2)
