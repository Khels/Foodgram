from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from ..models import Follow, Recipe, Tag
from .helpers import get_checked_tags

User = get_user_model()


def recipe_author(request, username):
    author = get_object_or_404(User, username=username)
    tags = Tag.objects.all()
    checked_tags = get_checked_tags(request.GET)
    recipes = Recipe.objects.prefetch_related('author', 'tags').filter(
        author=author, tags__in=checked_tags).distinct()
    paginator = Paginator(recipes, settings.PAGINATE_BY)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    is_subscribed = None
    if request.user.is_authenticated:
        is_subscribed = Follow.objects.filter(
            author=author, subscriber=request.user).exists()
    return render(
        request,
        'recipes/authorRecipe.html',
        {'page': page, 'paginator': paginator, 'is_subscribed': is_subscribed,
         'tags': tags, 'checked_tags': checked_tags, 'author': author}
    )
