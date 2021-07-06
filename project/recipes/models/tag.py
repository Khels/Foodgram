from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    name = models.CharField(
        _('тег'),
        primary_key=True,
        max_length=200,
    )
    color = models.CharField(
        _('цвет тега'),
        max_length=50,
        blank=False,
        null=False,
    )
    slug = models.SlugField(
        _('тег (англ.)'),
        max_length=200,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _('тег')
        verbose_name_plural = _('теги')
        ordering = ['name', 'slug']

    def __str__(self):
        return self.slug
