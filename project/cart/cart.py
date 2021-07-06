from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.utils.timezone import now

from recipes.models import Recipe
from cart import models


class CartIsEmpty(Exception):
    '''
    Occurs when you're trying to remove an item from an empty cart.
    '''
    pass


class Cart:
    def __init__(self, request):
        cart_id = request.session.get(settings.CART_ID)
        try:
            user = request.user if request.user.is_authenticated else None
            cart = models.Cart.objects.get(
                Q(id=cart_id) | Q(customer=user))
        except ObjectDoesNotExist:
            cart = self.new(request)
        self.cart = cart

    def __iter__(self):
        for recipe in self.cart.recipes.all():
            yield recipe

    def new(self, request):
        if request.user.is_authenticated:
            cart = models.Cart.objects.create(
                customer=request.user,
                creation_date=now(),
            )
        else:
            cart = models.Cart.objects.create(
                creation_date=now(),
            )
        request.session[settings.CART_ID] = cart.id
        return cart

    def add(self, recipe_id):
        '''
        Raises ObjectDoesNotExist if no recipe was found.

        There's no exception handling because the view should respond
        to a request accordingly with operation success=True/False.
        '''
        recipe = Recipe.objects.get(id=recipe_id)
        self.cart.recipes.add(recipe)

    def remove(self, recipe_id):
        '''
        Raises ObjectDoesNotExist if no recipe was found
        or CartIsEmpty if there were no recipes in cart.

        There's no exception handling because the view should respond
        to a request accordingly with operation success=True/False.
        '''
        if self.is_empty:
            raise CartIsEmpty
        recipe = self.cart.recipes.get(id=recipe_id)
        self.cart.recipes.remove(recipe)

    def count(self):
        return self.cart.recipes.count()

    def clear(self):
        self.cart.recipes.all().delete()

    @property
    def is_empty(self):
        return self.count() == 0
