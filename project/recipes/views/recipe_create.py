from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ..forms import RecipeForm
from .save_ingredients import save_ingredients


def get_tags_from_request(request):
    from ..models import Tag
    if request.method == 'POST':
        tags = Tag.objects.filter(slug__in=dict(request.POST).get('tags')).all()
        return tags
    return []


def get_ingredients_from_request(request):
    from ..models import Ingredient
    ingredients = []
    for field, value in request.POST.items():
        if field.find('nameIngredient_', 0) != -1:
            _, ingredient_order = field.split('_')
            amount = request.POST['valueIngredient_' + ingredient_order]
            ingredient = Ingredient.objects.get(title=value)
            ingredients.append((ingredient, amount))
    return ingredients


@login_required
def recipe_create(request):
    '''
    Render the page with recipe creation form and
    save the passed ingredients separately.
    '''
    form = RecipeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.author = request.user
        recipe = form.save()
        save_ingredients(request, recipe)
        recipe.save()
        return redirect('recipe_view', recipe_id=recipe.id, slug=recipe.slug)
    print('\n\n\n\n', request.POST, '\n\n\n\n')
    # if the form is invalid do not lose user's input
    tags = get_tags_from_request(request)
    print('\n\n\n\n', tags, '\n\n\n\n')
    ingredients = get_ingredients_from_request(request)
    print('\n\n\n\n', ingredients, '\n\n\n\n')
    return render(
        request,
        'recipes/formRecipe.html',
        {'form': form, 'tags': tags, 'ingredients': ingredients},
    )
