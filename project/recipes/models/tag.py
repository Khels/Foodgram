from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    class Meta:
        ordering = ['name']
        verbose_name_plural = _('tags')
        verbose_name = _('tag')

    name = models.CharField(
        _('Тег'),
        primary_key=True,
        max_length=200,
    )

    def __str__(self):
        return self.name
