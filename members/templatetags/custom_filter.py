# your_app/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key, default=''):
    return dictionary.get(key, default)
