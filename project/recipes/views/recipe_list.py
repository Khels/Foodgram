from django.shortcuts import render

from ..models import Recipe, Tag
from .helpers import get_checked_tags, get_paginator_and_page


def recipe_list(request):
    tags = Tag.objects.all()
    checked_tags = get_checked_tags(request.GET)
    recipes = Recipe.objects.prefetch_related('tags').filter(
        tags__in=checked_tags).distinct()
    paginator, page = get_paginator_and_page(request, recipes)
    return render(
        request,
        'recipes/index.html',
        {'page': page, 'paginator': paginator,
         'tags': tags, 'checked_tags': checked_tags}
    )
