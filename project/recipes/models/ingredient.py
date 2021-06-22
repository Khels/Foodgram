from django.db import models
from django.utils.translation import gettext_lazy as _


class Ingredient(models.Model):
    class Meta:
        verbose_name_plural = _('ingredients')
        verbose_name = _('ingredient')
        ordering = ['title']

    title = models.CharField(
        _('Название'),
        max_length=200
    )
    dimension = models.CharField(
        _('Единицы измерения'),
        max_length=200
    )

    def __str__(self):
        return self.title
