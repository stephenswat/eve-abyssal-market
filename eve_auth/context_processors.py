def user_eve_characters(request):
    if not request.user.is_authenticated:
        return {"eve_characters": {}}

    return {
        "eve_characters": {
            x.character_id: {"name": x.name} for x in request.user.characters.all()
        }
    }
