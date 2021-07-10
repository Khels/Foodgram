from django import forms

from ..models import Recipe, Tag


class RecipeForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        to_field_name='slug',
    )

    class Meta:
        model = Recipe
        fields = [
            'name',
            'image',
            'description',
            'tags',
            'cooking_time',
        ]

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = self.cleaned_data
        name_field = 'name'
        name = cleaned_data.get(name_field)
        if name:
            if Recipe.objects.filter(name=name, author=self.author).exists():
                self.add_error(
                    name_field, 'У вас уже есть рецепт с таким названием!')
        return cleaned_data
