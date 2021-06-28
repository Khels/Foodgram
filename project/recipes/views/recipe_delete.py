from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Recipe


@login_required
def recipe_delete(request, recipe_id, slug):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if slug is None or recipe.slug != slug:
        return redirect('recipe_delete', recipe_id=recipe_id, slug=recipe.slug)
    if request.user != recipe.author:
        return redirect('recipe_delete', recipe_id=recipe_id, slug=recipe.slug)
    recipe.delete()
    return redirect('recipe_list')
