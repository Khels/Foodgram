from django.shortcuts import render

from cart.cart import Cart


def purchase_list(request):
    '''
    Render the shopping list page.
    '''
    return render(
        request,
        'recipes/shop_list.html',
        {
            'cart': Cart(request),
        }
    )
