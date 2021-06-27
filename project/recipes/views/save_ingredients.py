from ..models import Ingredient, RecipeIngredient

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
            RecipeIngredient.objects.get_or_create(
                ingredient=ingredient,
                amount=ingredient_amount,
                recipe=recipe,
            )

            # if not RecipeIngredient.objects.filter(
            #         ingredient=ingredient, recipe=recipe).exists():
            #     RecipeIngredient.objects.create(
            #         ingredient=ingredient,
            #         amount=ingredient_amount,
            #         recipe=recipe,
            #     )
            # else:
            #     recipe_ingredient = get_object_or_404(
            #         RecipeIngredient,
            #         recipe=recipe,
            #         ingredient=ingredient,
            #     )
            #     recipe_ingredient.amount = ingredient_amount
            #     recipe_ingredient.save()
