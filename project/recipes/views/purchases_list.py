from django.http.response import HttpResponse

from cart.models import Cart


def purchases_list(request):
    return HttpResponse(str(dict(request.session)))
