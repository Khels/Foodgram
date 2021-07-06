from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Follow(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscribers',
        verbose_name=_('автор'),
    )
    subscriber = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
        verbose_name=_('подписчик'),
    )

    class Meta:
        verbose_name = _('подписка')
        verbose_name_plural = _('подписки')
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'subscriber'], name='unique_follow')
        ]

    def __str__(self):
        return f'{self.subscriber.username} to {self.author.username}'
