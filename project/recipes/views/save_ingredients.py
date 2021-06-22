from django.shortcuts import get_object_or_404

from ..models import Ingredient, RecipeIngredient


def save_ingredients(request, recipe):
    for field, value in request.POST.items():
        if field.find('nameIngredient', 0) != -1:
            field_split = field.split('_')
            ingredient = get_object_or_404(Ingredient, title=value)
            if not RecipeIngredient.objects.filter(
                    ingredient=ingredient, recipe=recipe).exists():
                RecipeIngredient.objects.create(
                    ingredient=ingredient,
                    amount=request.POST[
                        'valueIngredient_' + f'{field_split[1]}'
                    ],
                    recipe=recipe,
                )
            else:
                recipe_ingredient = get_object_or_404(
                    RecipeIngredient,
                    recipe=recipe,
                    ingredient=ingredient,
                )
                recipe_ingredient.amount = (
                    recipe_ingredient.amount + int(
                        request.POST['valueIngredient_' + f'{field_split[1]}']
                    )
                )
                recipe_ingredient.save()
