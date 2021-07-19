from django.http import HttpResponse

from cart.cart import Cart


def purchase_download(request):
    '''
    Return the PDF-converted shopping list.
    '''
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = (
        'attachment; filename="shopping-list.pdf"')
    cart = Cart(request)
    pdf = cart.convert_to_pdf()
    response.write(pdf)
    return response
