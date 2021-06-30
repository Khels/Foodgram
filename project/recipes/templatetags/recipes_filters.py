from django import template

register = template.Library()


@register.filter
def trunc_params(url):
    qmark_idx = url.find('?')
    return url[:qmark_idx] if qmark_idx != -1 else url
