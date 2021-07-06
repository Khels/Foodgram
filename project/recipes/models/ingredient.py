from django.db import models
from django.utils.translation import gettext_lazy as _


class Ingredient(models.Model):
    title = models.CharField(
        _('название'),
        max_length=200
    )
    dimension = models.CharField(
        _('единицы измерения'),
        max_length=200
    )

    class Meta:
        verbose_name = _('ингредиент')
        verbose_name_plural = _('ингредиенты')
        ordering = ['title']

    def __str__(self):
        return self.title
