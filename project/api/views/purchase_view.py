from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.cart import CartIsEmpty

User = get_user_model()


class PurchaseView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({'success': True})

    def post(self, request):
        recipe_id = request.data.get('id')
        cart = request.cart
        try:
            cart.add(recipe_id)
        except ObjectDoesNotExist:
            return Response({'success': False})
        return Response({'success': True})

    def delete(self, request, recipe_id):
        cart = request.cart
        try:
            cart.remove(recipe_id)
        except (ObjectDoesNotExist, CartIsEmpty):
            return Response({'success': False})
        return Response({'success': True})
