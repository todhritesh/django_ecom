from django import template 

register = template.Library()


@register.filter
def multiply(val1, val2):
    return float(val1) * float(val2)