from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from recipes.forms import RecipeForm
from recipes.views.helpers import (get_ingredients_from_request,
                                   get_tags_from_request, save_ingredients)


@login_required
def recipe_create(request):
    '''
    Render the page with recipe creation form and
    save the passed ingredients separately.
    '''
    form = RecipeForm(
        request.POST or None, request.FILES or None, author=request.user)
    if form.is_valid():
        form.instance.author = request.user
        recipe = form.save()
        save_ingredients(request, recipe)
        recipe.save()
        return redirect('recipe_view', recipe_id=recipe.id, slug=recipe.slug)
    # if the form is invalid do not lose user's chosen tags and ingredients
    tags = get_tags_from_request(request)
    ingredients = get_ingredients_from_request(request)
    return render(
        request,
        'recipes/formRecipe.html',
        {'form': form, 'tags': tags, 'ingredients': ingredients},
    )
