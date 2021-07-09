from django.shortcuts import render


def purchase_list(request):
    return render(
        request,
        'recipes/shopList.html',
        {
            'cart': request.cart,
        }
    )
