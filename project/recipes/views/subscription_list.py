from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from recipes.views.helpers import get_paginator_and_page


@cache_page(7)
@login_required
def subscription_list(request):
    '''
    Renders the page with user's subscriptions.
    '''
    subscriptions = request.user.subscriptions.annotate(
        num_recipes=Count('author__recipes') - 3).order_by('-id')
    paginator, page = get_paginator_and_page(request, subscriptions)
    return render(
        request,
        'recipes/my_follow.html',
        {'page': page, 'paginator': paginator},
    )
