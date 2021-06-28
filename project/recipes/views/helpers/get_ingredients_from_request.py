from ...models import Ingredient


def get_ingredients_from_request(request):
    ingredients = []
    for field, value in request.POST.items():
        if field.find('nameIngredient_', 0) != -1:
            _, ingredient_order = field.split('_')
            amount = request.POST['valueIngredient_' + ingredient_order]
            ingredient = Ingredient.objects.get(title=value)
            ingredients.append((ingredient, amount))
    return ingredients
