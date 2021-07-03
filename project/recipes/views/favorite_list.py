from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .helpers import get_paginator_and_page, get_tags_and_checked_tags


@login_required
def favorite_list(request):
    tags, checked_tags = get_tags_and_checked_tags(request)
    favorites = request.user.favorites.filter(
        recipe__tags__in=checked_tags)
    favorite_recipes = [favorite.recipe for favorite in favorites]
    paginator, page = get_paginator_and_page(request, favorite_recipes)
    return render(
        request,
        'recipes/favorite.html',
        {
            'page': page,
            'paginator': paginator,
            'tags': tags,
            'checked_tags': checked_tags,
        },
    )
