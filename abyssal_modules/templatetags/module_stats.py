from django import template


register = template.Library()


@register.filter
def get_attribute_value(mod, attr):
    return mod.get_value(attr)
