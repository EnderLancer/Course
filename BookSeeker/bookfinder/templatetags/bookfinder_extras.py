from urllib.parse import urlencode
from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.copy()
    print(kwargs)
    for key, value in kwargs.items():
        query[key] = value
    return query.urlencode()
