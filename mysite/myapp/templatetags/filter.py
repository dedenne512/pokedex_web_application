from django import template
register = template.Library()

@register.filter
def get_name(dic, key):
    print(dic.get(key))
    return dic.get(key)