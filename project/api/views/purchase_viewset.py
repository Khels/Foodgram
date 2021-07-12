from cart.cart import CartIsEmpty
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

User = get_user_model()


class PurchaseViewset(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        recipe_id = request.data.get('id')
        cart = request.cart
        try:
            cart.add(recipe_id)
        except ObjectDoesNotExist:
            return Response({'success': False})
        return Response({'success': True})

    def destroy(self, request, pk):
        cart = request.cart
        try:
            cart.remove(pk)
        except (ObjectDoesNotExist, CartIsEmpty):
            return Response({'success': False})
        return Response({'success': True})
