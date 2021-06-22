from django.shortcuts import get_object_or_404, redirect, render

from ..models import Recipe, Follow


def recipe_view(request, recipe_id, slug=None):
    '''Render one recipe'''
    recipe = get_object_or_404(Recipe, id=recipe_id)
    # check if a passed (or not passed at all) slug corresponds to recipe id
    # otherwise redirect to a url with correct id/slug relation
    if slug is None or recipe.slug != slug:
        return redirect('recipe_view', recipe_id=recipe_id, slug=recipe.slug)
    tags = recipe.tags.all()
    recipe_ingredient = recipe.recipe_ingredient.all()
    is_subscribed = None
    if request.user.is_authenticated:
        is_subscribed = Follow.objects.filter(
            author=recipe.author, subscriber=request.user).exists()
    return render(
        request,
        'recipes/singlePage.html',
        {
            'author': recipe.author,
            'recipe': recipe,
            'tags': tags,
            'recipe_ingredient': recipe_ingredient,
            'is_subscribed': is_subscribed,
        }
    )
