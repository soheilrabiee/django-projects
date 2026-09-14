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
        # Add placeholder and set required field for the form
        widgets = {
            "item_name": forms.TextInput(attrs={"placeholder": "e.g Margherita Pizza", "required": True}),
            "item_desc": forms.TextInput(attrs={"placeholder": "e.g Fresh and cheesy", "required": True}),
            "item_price": forms.NumberInput(attrs={"placeholder": "100", "required": True}),
            "item_image": forms.URLInput(attrs={"required": False}),
        }
