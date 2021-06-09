from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from ..models import Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/indexNotAuth.html'
    context_object_name = 'recipes'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(RecipeListView, self).get_context_data(**kwargs)
        recipes = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(recipes, self.paginate_by)
        try:
            recipes = paginator.page(page)
        except PageNotAnInteger:
            recipes = paginator.page(1)
        except EmptyPage:
            recipes = paginator.page(paginator.num_pages)
        context['recipes'] = recipes
        return context
