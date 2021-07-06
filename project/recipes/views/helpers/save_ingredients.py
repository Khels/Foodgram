from recipes.models import Ingredient, RecipeIngredient

NAME_INGR = 'nameIngredient_'
VALUE_INGR = 'valueIngredient_'


def save_ingredients(request, recipe):
    '''
    Validate and save passed ingredients.
    The query has the following structure:

    'nameIngredient_1': ['Яйцо'], 'valueIngredient_1': ['4'],
    'unitsIngredient_1': ['шт.']
    '''
    for field, value in request.POST.items():
        if field.find(NAME_INGR, 0) != -1:
            _, ingredient_order = field.split('_')
            ingredient = Ingredient.objects.get(title=value)
            ingredient_amount = request.POST[VALUE_INGR + ingredient_order]
            recipe_ingredient, _ = RecipeIngredient.objects.get_or_create(
                ingredient=ingredient,
                recipe=recipe,
            )
            recipe_ingredient.amount += int(ingredient_amount)
            recipe_ingredient.save()
