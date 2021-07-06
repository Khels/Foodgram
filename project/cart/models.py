from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Cart(models.Model):
    customer = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('покупатель'),
        null=True,
    )
    recipes = models.ManyToManyField(
        'recipes.Recipe',
        related_name='carts',
        verbose_name=_('рецепты'),
    )
    creation_date = models.DateTimeField(
        _('дата создания'),
        editable=False,
    )

    class Meta:
        verbose_name = _('корзина')
        verbose_name_plural = _('корзины')
        ordering = ['-creation_date']

    def __str__(self):
        return str(self.creation_date)
