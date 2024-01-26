def format_attribute_basic(val, attr):
    if attr == 64:
        return "%.3f" % val
    elif attr == 105:
        return "%.0f" % val
    elif attr == 204:
        return "%.2f" % val
    else:
        return "%.1f" % val

def render_attribute_value(val, attr):
    if attr == 73:
        return 0.001 * val
    elif attr == 1795:
        return 0.001 * val
    elif attr == 147:
        return 100 * val
    elif attr == 213:
        return 100 * (val - 1)
    elif attr == 204:
        return 100 * (1 - val)
    elif attr == 974:
        return 100 * (1 - val)
    elif attr == 975:
        return 100 * (1 - val)
    elif attr == 976:
        return 100 * (1 - val)
    elif attr == 977:
        return 100 * (1 - val)
    else:
        return val

def correct_high_is_good(val, attr):
    if attr == 204:
        return not val
    elif attr == 974:
        return not val
    elif attr == 975:
        return not val
    elif attr == 976:
        return not val
    elif attr == 977:
        return not val
    else:
        return val
