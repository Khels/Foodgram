from django.shortcuts import get_object_or_404, render

from recipes.models import Recipe
from recipes.views.helpers import check_slug


@check_slug('recipe_view')
def recipe_view(request, recipe_id, slug=None):
    '''Render one recipe'''
    recipe = get_object_or_404(Recipe, id=recipe_id)
    tags = recipe.tags.all()
    recipe_ingredient = recipe.recipe_ingredient.all()
    return render(
        request,
        'recipes/singlePage.html',
        {
            'author': recipe.author,
            'recipe': recipe,
            'tags': tags,
            'recipe_ingredient': recipe_ingredient,
        }
    )
