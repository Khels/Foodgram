from django import forms

from .. import models


class RecipeForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=models.Tag.objects.all(),
                                          to_field_name='slug')

    class Meta:
        model = models.Recipe
        fields = [
            'name',
            'image',
            'description',
            'tags',
            'cooking_time',
        ]
