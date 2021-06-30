from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render

from ..models import Recipe, Tag
from .helpers import get_checked_tags


def recipe_list(request):
    tags = Tag.objects.all()
    checked_tags = get_checked_tags(request.GET)
    recipes = Recipe.objects.prefetch_related('tags').filter(
        tags__in=checked_tags).distinct()
    paginator = Paginator(recipes, settings.PAGINATE_BY)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'recipes/index.html',
        {'page': page, 'paginator': paginator,
         'tags': tags, 'checked_tags': checked_tags}
    )
