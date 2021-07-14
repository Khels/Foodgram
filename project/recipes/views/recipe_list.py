from django.shortcuts import render
from django.views.decorators.cache import cache_page

from recipes.models import Recipe
from recipes.views.helpers import (get_paginator_and_page,
                                   get_tags_and_checked_tags)


@cache_page(7)
def recipe_list(request):
    '''
    Renders the index page.
    '''
    tags, checked_tags = get_tags_and_checked_tags(request)
    recipes = Recipe.objects.prefetch_related('tags').filter(
        tags__in=checked_tags).distinct()
    paginator, page = get_paginator_and_page(request, recipes)
    return render(
        request,
        'recipes/index.html',
        {
            'page': page,
            'paginator': paginator,
            'tags': tags,
            'checked_tags': checked_tags,
        }
    )
