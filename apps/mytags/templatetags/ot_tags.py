import datetime
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(is_safe=True)
def ot_cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')

@register.filter(is_safe=False)
@stringfilter
def ot_lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)