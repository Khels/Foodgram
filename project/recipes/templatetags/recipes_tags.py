from django import template

register = template.Library()


@register.simple_tag
def choose_tag(request, tag):
    '''
    Append tag=<tag.slug> parameter to a URL if no such tag was already passed
    otherwise delete such tag parameter from URL.
    '''
    if request.GET:
        if tag not in request.GET.getlist('tag'):
            return request.get_full_path() + f'&tag={tag}'
        else:
            return request.get_full_path().replace(f'&tag={tag}', '')
    return request.get_full_path() + f'?tag={tag}'


@register.simple_tag
def preserve_tags(request, page_number):
    '''
    Given a request like this /?page=1&tags=lunch&tags=dinner
    change the page number preserving other parameters however.
    '''
    if request.GET:
        page_value = request.GET.get('page')
        if not page_value:
            return request.get_full_path().replace(
                '?', f'?page={page_number}&')
        else:
            return request.get_full_path().replace(
                f'page={page_value}', f'page={page_number}')
    return request.get_full_path() + f'?page={page_number}'
