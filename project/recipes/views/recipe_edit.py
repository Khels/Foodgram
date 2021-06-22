from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .. import views
from ..forms import RecipeForm
from ..models import Recipe

# <QueryDict: {'csrfmiddlewaretoken': ['mveMepYbW5cGIrsqkpTY6oqvGE3P02FZieEzghZ75hJINRbPnkNhDq8Beh6VEHsN'],
# 'name': ['Яичница'], 'breakfast': ['on'], 'nameIngredient_1': ['Яйцо'], 'valueIngredient_1': ['4'],
# 'unitsIngredient_1': ['шт.'], 'cooking_time': ['7'], 'description': ['Найс']}>


@login_required
def recipe_edit(request, recipe_id, slug):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    # check if a passed (or not passed at all) slug corresponds to recipe id
    # otherwise redirect to a url with correct id/slug relation
    if slug is None or recipe.slug != slug:
        return redirect('recipe_view', recipe_id=recipe_id, slug=recipe.slug)
    if request.user != recipe.author:
        return redirect('recipe_view', recipe_id=recipe_id, slug=recipe.slug)
    print('\n\n\n\n', request.POST, '\n\n\n\n')
    form = RecipeForm(
        request.POST or None,
        request.FILES or None,
        instance=recipe,
    )
    print(form.errors)
    if not form.is_valid():
        return render(
            request,
            'recipes/formRecipe.html',
            {'form': form},
        )
    recipe = form.save()
    views.save_ingredients(request, recipe)
    recipe.save()
    return redirect('recipe_list')
