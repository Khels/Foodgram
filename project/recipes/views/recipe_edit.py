from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from ..forms import RecipeForm
from ..models import Recipe
from .save_ingredients import save_ingredients


@login_required
def recipe_edit(request, recipe_id, slug):
    '''
    Render the page with recipe edit form and
    save edited/newly added ingredients separately.
    '''
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
            'recipes/formChangeRecipe.html',
            {'form': form},
        )
    recipe = form.save()
    save_ingredients(request, recipe)
    recipe.save()
    return redirect('recipe_list')
