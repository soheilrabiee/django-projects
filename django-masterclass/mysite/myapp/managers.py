from django.db import models


# Custom Item model manager
class ItemManager(models.Manager):
    # Adding new methods for the Item model
    def cheap_items(self):
        return self.filter(item_price__lt=5)

    def expensive_items(self):
        return self.filter(item_price__gt=5)

    def search(self, keyword):
        return self.filter(item_name__icontains=keyword)
