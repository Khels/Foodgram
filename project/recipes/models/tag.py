from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    class Meta:
        ordering = ['name', 'slug']
        verbose_name_plural = _('tags')
        verbose_name = _('tag')

    name = models.CharField(
        _('Тег'),
        primary_key=True,
        max_length=200,
    )
    color = models.CharField(
        _('Цвет тега'),
        max_length=50,
        blank=False,
        null=False,
    )
    slug = models.SlugField(
        _('Тег (англ.)'),
        max_length=200,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name
