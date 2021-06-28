from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
# from django.utils.translation import gettext_lazy as _


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        'recipes.Recipe',
        on_delete=models.SET_NULL,
        related_name='recipe_ingredient',
        null=True,
    )
    ingredient = models.ForeignKey(
        'recipes.Ingredient',
        on_delete=models.SET_NULL,
        related_name='recipe_ingredient',
        blank=True,
        null=True,
    )
    amount = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100000),
        ]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique_recipeingredient'
            )
        ]

    def __str__(self):
        return f'{self.recipe.name}, {self.ingredient.title}, {self.amount}'

    def __repr__(self):
        return str(self)
