from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ..forms import RecipeForm
from .. import views

# <QueryDict: {'csrfmiddlewaretoken': ['mveMepYbW5cGIrsqkpTY6oqvGE3P02FZieEzghZ75hJINRbPnkNhDq8Beh6VEHsN'],
# 'name': ['Яичница'], 'breakfast': ['on'], 'nameIngredient_1': ['Яйцо'], 'valueIngredient_1': ['4'],
# 'unitsIngredient_1': ['шт.'], 'cooking_time': ['7'], 'description': ['Найс']}>


@login_required
def recipe_create(request):
    print('\n\n\n\n', request.POST, '\n\n\n\n')
    form = RecipeForm(request.POST or None, request.FILES or None)
    print(form.errors)
    if not form.is_valid():
        return render(
            request,
            'recipes/formRecipe.html',
            {'form': form},
        )
    form.instance.author = request.user
    recipe = form.save()
    views.save_ingredients(request, recipe)
    recipe.save()
    return redirect('recipe_list')
