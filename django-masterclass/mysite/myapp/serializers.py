from rest_framework import serializers

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        # Use the Item model for this serializer
        model = Item
        # Fields exposed by the API
        fields = ["id", "item_name", "item_desc", "item_price", "item_image"]
