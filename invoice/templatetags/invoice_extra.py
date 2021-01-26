from django import template

register = template.Library()

@register.filter
def moneycent(values):
    return format(int(values), ',')
