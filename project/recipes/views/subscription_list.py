from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render

from .helpers import get_paginator_and_page


@login_required
def subscription_list(request):
    subscriptions = request.user.subscriptions.annotate(
        num_recipes=Count('author__recipes') - 3)
    paginator, page = get_paginator_and_page(request, subscriptions)
    return render(
        request,
        'recipes/myFollow.html',
        {'page': page, 'paginator': paginator},
    )
