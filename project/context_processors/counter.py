from cart.cart import Cart


def counter(request):
    '''
    Returns the current amount of recipes in user's shopping list.
    '''
    cart = Cart(request)
    return {'counter': cart.count()}
