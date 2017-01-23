from django import template

register = template.Library()

@register.filter
@stringfilter
def fix_name(value):
    return value.replace(' ','_')
