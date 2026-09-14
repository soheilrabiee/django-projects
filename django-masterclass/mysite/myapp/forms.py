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

    # Add methods to the class to validate field values
    # Should be named as clean_[field name]
    def clean_item_price(self):
        # Gets cleaned form data
        price = self.cleaned_data["item_price"]
        if price < 0:
            raise forms.ValidationError("Price cannot be negative")
        return price

    # Form level validation
    def clean(self):
        # Performs Django's normal form cleaning and returns cleaned results
        cleaned_data = super().clean()
        name = cleaned_data.get("item_name")
        desc = cleaned_data.get("item_desc")
        if name and desc and name.lower() in desc.lower():
            self.add_error("item_desc", "Description should add new info beyond the name")
        return cleaned_data
