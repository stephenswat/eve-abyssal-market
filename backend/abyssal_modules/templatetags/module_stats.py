from django import template


register = template.Library()


@register.filter
def format_attribute(mod, attr):
    val = mod.get_value(attr)

    if attr == 64:
        return "%.3f" % val
    elif attr == 105:
        return "%.0f" % val
    else:
        return "%.1f" % val

@register.filter
def format_attribute_basic(val, attr):
    if attr == 64:
        return "%.3f" % val
    elif attr == 105:
        return "%.0f" % val
    else:
        return "%.1f" % val

@register.filter()
def delta(d, attr):
    return d.get(attr, None)["delta"]
