from django import template

from abyssal_modules.utils import (
    format_attribute_basic as fb,
    render_attribute_value as rv,
    correct_high_is_good as hg
)


register = template.Library()


@register.filter
def format_attribute(mod, attr):
    val = mod.get_value(attr)

    return fb(rv(val, attr), attr)


@register.filter
def format_attribute_basic(val, attr):
    return fb(val, attr)

@register.filter
def rendered_high_is_good(at):
    return hg(at.id, at.high_is_good)

@register.filter()
def delta(d, attr):
    return d.get(attr, None)["delta"]
