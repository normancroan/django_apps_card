from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def fix_name(value):
    return value.replace(' ','_')
