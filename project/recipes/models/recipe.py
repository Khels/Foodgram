from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from pytils.translit import slugify


class Recipe(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name=_('автор'),
    )
    name = models.CharField(
        _('название'),
        max_length=200,
    )
    pub_date = models.DateTimeField(
        _('дата публикации'),
        auto_now_add=True,
        db_index=True,
    )
    image = models.ImageField(
        _('картинка'),
        upload_to='recipes/',
    )
    description = models.TextField(
        _('описание'),
    )
    ingredients = models.ManyToManyField(
        'recipes.Ingredient',
        related_name='recipes',
        through='recipes.RecipeIngredient',
        verbose_name=_('ингредиенты'),
    )
    tags = models.ManyToManyField(
        'recipes.Tag',
        related_name='recipes',
        verbose_name=_('теги'),
    )
    cooking_time = models.IntegerField(
        _('время приготовления'),
        validators=[
            MinValueValidator(5),
            MaxValueValidator(400),
        ]
    )
    slug = models.SlugField(
        _('название (англ.)'),
        max_length=200,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _('рецепт')
        verbose_name_plural = _('рецепты')
        ordering = ['-pub_date']
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'name'],
                name='unique_recipe',
            )
        ]

    def __str__(self):
        return f'{self.name}, {self.author}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Recipe, self).save(*args, **kwargs)
