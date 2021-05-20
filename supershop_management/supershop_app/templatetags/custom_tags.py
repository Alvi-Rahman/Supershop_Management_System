from django import template

register = template.Library()


@register.filter(name='calculate_total_price')
def calculate_total_price(price, unit):
    pass
