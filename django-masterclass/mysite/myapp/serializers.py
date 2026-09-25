from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Item


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class ItemSerializer(serializers.ModelSerializer):
    # user_name = serializers.StringRelatedField()
    # Pass the whole User object as nested into the JSON in our API
    user_name = UserSerializer(read_only=True)

    class Meta:
        # Use the Item model for this serializer
        model = Item
        # Fields exposed by the API
        fields = ["id", "user_name", "item_name", "item_desc", "item_price", "item_image"]

    # validate_<field_name> to name the method and perform field level validation
    def validate_item_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be greater than zero!")
        return value
