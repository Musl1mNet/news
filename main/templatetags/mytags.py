from django import template
import re
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag()
def find(request, num):
    list1 = re.findall(r'\d+', request.GET.get("numbers"))

    try:
        return list1[num]
    except IndexError:
        return "Buday index yo'q"

@register.simple_tag()
def send_tag(strs):
    str = strs.split(";")
    send = f'<h1>{str[0]}</h1>\n<h1>{str[1]}</h1>'
    return mark_safe(send)