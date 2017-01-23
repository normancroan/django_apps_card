from django import template

register = template.Libray()

@register.filter
@stringfilter
def fix_name(value):
    return value.replace(' ','_')
