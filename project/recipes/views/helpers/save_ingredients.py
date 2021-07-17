from django.forms import ValidationError

from recipes.models import Ingredient, RecipeIngredient

NAME_INGR = 'nameIngredient_'
VALUE_INGR = 'valueIngredient_'


def save_ingredients(request, recipe):
    '''
    Validates and saves passed ingredients.
    The query has the following structure:

    'nameIngredient_1': ['Яйцо'], 'valueIngredient_1': ['4'],
    'unitsIngredient_1': ['шт.']
    '''
    ingr_cnt = 0
    for field, value in request.POST.items():
        if field.find(NAME_INGR, 0) != -1:
            name, ingredient_order = field.split('_')
            ingredient = Ingredient.objects.get(title=value)
            ingredient_amount = request.POST[VALUE_INGR + ingredient_order]
            rec_ingr, created = RecipeIngredient.objects.get_or_create(
                ingredient=ingredient,
                recipe=recipe,
            )
            if created:
                rec_ingr.amount = int(ingredient_amount)
            else:
                rec_ingr.amount += int(ingredient_amount)
            rec_ingr.save()
            ingr_cnt += 1
    if ingr_cnt == 0:
        raise ValidationError(
            'Вы должны добавить как минимум один ингредиент!'
        )
