from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.cart import Cart, CartIsEmpty

User = get_user_model()


class PurchaseView(APIView):
    def get(self, request):
        return Response({'success': True})

    def post(self, request):
        recipe_id = request.data.get('id')
        cart = Cart(request)
        try:
            cart.add(recipe_id)
        except ObjectDoesNotExist:
            return Response({'success': False})
        return Response({'success': True})

    def delete(self, request, recipe_id):
        cart = Cart(request)
        try:
            cart.remove(recipe_id)
        except (ObjectDoesNotExist, CartIsEmpty):
            return Response({'success': False})
        return Response({'success': True})
