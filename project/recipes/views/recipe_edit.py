from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from ..forms import RecipeForm
from ..models import Recipe, RecipeIngredient
from .helpers import get_ingredients_from_request, get_tags_from_request
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
        return redirect('recipe_edit', recipe_id=recipe_id, slug=recipe.slug)
    if request.user != recipe.author:
        return redirect('recipe_view', recipe_id=recipe_id, slug=recipe.slug)
    form = RecipeForm(
        request.POST or None,
        request.FILES or None,
        instance=recipe,
    )
    if form.is_valid():
        recipe = form.save()
        # delete old recipe's ingredients
        RecipeIngredient.objects.filter(recipe=recipe).delete()
        save_ingredients(request, recipe)  # save updated ingredients
        recipe.save()
        return redirect('recipe_view', recipe_id=recipe_id, slug=recipe.slug)
    tags = recipe.tags.all()
    recipe_ingredients = RecipeIngredient.objects.filter(recipe=recipe).all()
    if request.method == 'POST':
        tags = get_tags_from_request(request)
        ingredients = get_ingredients_from_request(request)
    return render(
        request,
        'recipes/formChangeRecipe.html',
        {'form': form, 'tags': tags, 'recipe': recipe,
         'recipe_ingredients': recipe_ingredients},
    )
