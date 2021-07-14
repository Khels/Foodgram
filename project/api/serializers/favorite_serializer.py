from django.contrib.auth import get_user_model

from recipes.models import Favorite, Recipe

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

User = get_user_model()


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )
    recipe = serializers.PrimaryKeyRelatedField(
        queryset=Recipe.objects.all(),
    )

    class Meta:
        fields = ('__all__')
        model = Favorite
        validators = [
            UniqueTogetherValidator(
                queryset=Favorite.objects.all(),
                fields=['user', 'recipe']
            )
        ]
