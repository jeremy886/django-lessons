__author__ = 'Jeremy Chen'

from django import template
import datetime

register = template.Library()

@register.inclusion_tag('show_time2.html', takes_context=True)
def mytime(context):
    return {
        'time_loal': context['time_local'],
        'time_taipei': context['time_taipei']
    }

@register.assignment_tag
def get_current_time(format_string):
    return datetime.datetime.now().strftime(format_string)