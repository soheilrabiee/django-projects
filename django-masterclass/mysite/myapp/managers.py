from django.db import models


# Custom manager for the item model
class ItemManager(models.Manager):
    # Override Django's default queryset to exclude soft-deleted objects
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
