from django.shortcuts import redirect


def check_slug(to, recipe, slug):
    # check if a passed (or not passed at all) slug corresponds to recipe id
    # otherwise redirect to a <to> url with correct id/slug relation
    if slug is None or recipe.slug != slug:
        return redirect(to=to, recipe_id=recipe.id, slug=recipe.slug)
