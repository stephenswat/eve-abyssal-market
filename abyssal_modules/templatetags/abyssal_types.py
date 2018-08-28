from django import template


register = template.Library()


@register.simple_tag
def get_abyssal_type_list():
    return [
        ("Microwarpdrives", [("5MN", 47740), ("50MN", 47408), ("500MN", 47745)]),
        ("Afterburners", [("1MN", 47749), ("10MN", 47753), ("100MN", 47757)]),
        ("Shield Extenders", [("Small", 47800), ("Medium", 47804), ("Large", 47808)]),
        ("Armor Plates", [("Small", 47812), ("Medium", 47817), ("Large", 47820)]),
        ("Shield Boosters", [("Small", 47781), ("Medium", 47785), ("Large", 47789), ("X-Large", 47793)]),
        ("Armor Repairers", [("Small", 47769), ("Medium", 47773), ("Large", 47777)]),
        ("Ancil. Shield Boosters", [("Medium", 47836), ("Large", 47838), ("X-Large", 47840)]),
        ("Ancil. Armor Repairers", [("Small", 47842), ("Medium", 47844), ("Large", 47846)]),
        ("Energy Neutralizers", [("Small", 47824), ("Medium", 47828), ("Heavy", 47832)]),
        ("Tackle Modules", [("Stasis Webifiers", 47702), ("Warp Scramblers", 47732), ("Warp Disruptors", 47736)]),
    ]

@register.filter()
def column_width(l):
    return 12 // len(l)
