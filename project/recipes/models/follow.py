from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Follow(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'subscriber'], name='unique_follow')
        ]
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='subscribers',
        null=True,
    )
    subscriber = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='subscriptions',
        null=True,
    )
