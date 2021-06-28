from recipes.models import Tag


def get_checked_tags(query):
    '''
    Take request.GET and return tags checked by user or all tags existing.
    '''
    checked_tags = Tag.objects.filter(slug__in=query.getlist('tag')).all()
    return checked_tags if checked_tags else Tag.objects.all()
