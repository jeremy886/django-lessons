__author__ = 'Jeremy Chen'

import datetime
from django import template
from pytz import timezone

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.simple_tag(takes_context=True)
def current_timezone_time(context, format_string):
    tz = context['timezone']
    new_time = datetime.datetime.now(timezone(tz))
    #print(new_time.astimezonestrftime("%c"))
    return new_time.strftime(format_string)

register.simple_tag(lambda author: "Copyright (c) 2016 by " + author, name='copyright')
