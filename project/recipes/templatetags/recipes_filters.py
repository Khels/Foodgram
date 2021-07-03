from django import template
from recipes.models import Favorite, Follow

register = template.Library()


@register.filter
def trunc_params(url):
    '''Return an absolute URL path without any query params.'''
    qmark_idx = url.find('?')
    return url[:qmark_idx] if qmark_idx != -1 else url


@register.filter
def is_favorite(recipe, user):
    '''Check if a given recipe is in user's favorites.'''
    return Favorite.objects.filter(user=user, recipe=recipe).exists()


@register.filter
def is_subscribed(user, author):
    '''Check if a given user is subscribed to another user (author).'''
    return Follow.objects.filter(author=author, subscriber=user).exists()
