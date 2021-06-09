from django.urls import path
from .views import RecipeListView

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/<int:recipe_id>/<slug:slug>/', views.recipe_view, name='recipe_view'),
]
