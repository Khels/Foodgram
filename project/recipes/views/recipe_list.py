from django.shortcuts import render

from ..models import Recipe
from .helpers import get_paginator_and_page, get_tags_and_checked_tags


def recipe_list(request):
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
