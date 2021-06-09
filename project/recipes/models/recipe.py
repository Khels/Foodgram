from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Recipe(models.Model):
    class Meta:
        verbose_name_plural = _('recipes')
        verbose_name = _('recipe')
        ordering = ['-pub_date']

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='recipes',
    )
    name = models.CharField(
        _('Название'),
        max_length=200,
    )
    pub_date = models.DateTimeField(
        _('Дата публикации'),
        auto_now_add=True,
        db_index=True,
    )
    image = models.ImageField(
        _('Картинка'),
        null=True,
        blank=True,
    )
    description = models.TextField(
        _('Описание'),
    )
    ingredients = models.ManyToManyField(
        'recipes.Ingredient',
        related_name='recipes',
        through='recipes.RecipeIngredient',
    )
    tags = models.ManyToManyField(
        'recipes.Tag',
    )
    cooking_time = models.IntegerField(
        validators=[
            MinValueValidator(5),
            MaxValueValidator(400),
        ]
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        default='slug',
    )

    def __str__(self):
        return f'{self.name}, {self.author}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Recipe, self).save(*args, **kwargs)
