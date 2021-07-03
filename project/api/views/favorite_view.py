from api.serializers import FavoriteSerializer
from django.shortcuts import get_object_or_404
from recipes.models import Favorite, Recipe
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class FavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        recipe_id = request.data.get('id')
        serializer = FavoriteSerializer(
            data={'user': request.user, 'recipe': recipe_id})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True})

    def delete(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        favorite = get_object_or_404(
            Favorite, user=request.user, recipe=recipe)
        favorite.delete()
        return Response({'success': True})
