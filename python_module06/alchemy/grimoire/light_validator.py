import alchemy.grimoire.light_spellbook as spell_b


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = spell_b.light_spell_allowed_ingredients()

    my_ingredients = [
        ingred.strip().lower()
        for ingred in ingredients.split(',')]

    for ingredient in allowed_ingredients:
        if ingredient.lower() in my_ingredients:
            return f"Spell recorded: {ingredients}:VALID"
    return f"Spell rejected: {ingredients}:INVALID"
