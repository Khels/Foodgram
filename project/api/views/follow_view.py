from api.serializers import FollowSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from recipes.models import Follow
from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()


class FollowView(APIView):
    def post(self, request):
        author_id = request.data.get('id')
        author = get_object_or_404(User, id=author_id)
        serializer = FollowSerializer(
            data={'author': author, 'subscriber': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True})

    def delete(self, request, id):
        author = get_object_or_404(User, id=id)
        follow = get_object_or_404(
            Follow, author=author, subscriber=request.user)
        follow.delete()
        return Response({'success': True})
