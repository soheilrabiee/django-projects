from django import forms

from .models import Item


# Inherit from modelform just like regular django models
class ItemForm(forms.ModelForm):
    # Which model the form is based on
    class Meta:
        # Generate the form from the Item model
        model = Item
        # Which fields of the model should be included or excluded
        fields = ["item_name", "item_desc", "item_price", "item_image"]
