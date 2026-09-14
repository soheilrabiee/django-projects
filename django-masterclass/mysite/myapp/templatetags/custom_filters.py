from django import template

register = template.Library()


# Register custom filters for templates
@register.filter
def currency(value):
    return f"${value}"


@register.filter
def discount(value, percentage):
    return int(value) - ((int(percentage) / 100) * int(value))
