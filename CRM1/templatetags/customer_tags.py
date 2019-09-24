from datetime import datetime
from django.template import Library

register = Library()
@register.simple_tag(takes_context=True)
def show_time(context):
    now = datetime.now().strftime(context['time_str'])
    return now

@register.inclusion_tag('students/ul.html', takes_context=True)
def show_ul(context):
    return {'cous': context['cous'], 'flag': context['flag']}
