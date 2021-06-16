from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields.related import ForeignKey

User = get_user_model()


class Favorite(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'], name='unique_favorite')
        ]
    user = ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
    )
    recipe = ForeignKey(
        'recipes.Recipe',
        on_delete=models.CASCADE,
        related_name='favorites',
    )
