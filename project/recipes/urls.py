from django.urls import path
from . import views
urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipes/<int:recipe_id>/', views.recipe_view, name='recipe_view'),
    path('recipes/<int:recipe_id>/<slug:slug>/',
         views.recipe_view, name='recipe_view'),

]
