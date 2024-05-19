from django import template

register = template.Library()

@register.filter
def currency_format(value):
    try:
        return "{:,.0f}".format(value)
    except (ValueError, TypeError):
        return value
