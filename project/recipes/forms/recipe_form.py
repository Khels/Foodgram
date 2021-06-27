from django import forms

from ..models import Recipe, Tag


class RecipeForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                          to_field_name='slug')

    class Meta:
        model = Recipe
        fields = [
            'name',
            'image',
            'description',
            'tags',
            'cooking_time',
        ]
