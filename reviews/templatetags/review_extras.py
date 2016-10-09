from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()



def cut(value, arg):
    return value.replace(arg,'')

register.filter('cut', cut)

@register.filter
def vowel_upper(value):
    new_value = ''
    for v in value:
        if v in 'aeiou':
            new_value += v.upper()
        else:
            new_value += v
    return new_value

@register.filter
@stringfilter
def lower(value):
    return value.lower()