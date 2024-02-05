from django import template

from abyssal_modules.utils import (
    format_attribute_basic as fb,
    render_attribute_value as rv,
)


register = template.Library()


@register.filter
def format_attribute(mod, attr):
    val = mod.get_value(attr)

    return fb(rv(val, attr), attr)


@register.filter
def format_attribute_basic(val, attr):
    return fb(val, attr)


@register.filter()
def delta(d, attr):
    return d.get(attr, None)["delta"]
