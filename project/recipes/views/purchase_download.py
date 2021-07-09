from django.http import HttpResponse


def purchase_download(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = (
        'attachment; filename="shopping-list.pdf"')
    pdf = request.cart.convert_to_PDF()
    response.write(pdf)
    return response
