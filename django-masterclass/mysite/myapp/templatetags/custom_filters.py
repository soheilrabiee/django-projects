from django import template

register = template.Library()


# Register a custom filter for templates
@register.filter
def currency(value):
    return f"${value}"
