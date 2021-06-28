from ...models import Tag


def get_tags_from_request(request):
    if request.method == 'POST':
        tags = Tag.objects.filter(
            slug__in=dict(request.POST).get('tags')
        ).all()
        return tags
    return []
