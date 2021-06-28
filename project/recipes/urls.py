from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('', include('api.urls')),
    path('recipes/<int:recipe_id>/', views.recipe_view, name='recipe_view'),
    path('recipes/<int:recipe_id>/<slug:slug>/',
         views.recipe_view, name='recipe_view'),
    path('recipes/<int:recipe_id>/<slug:slug>/edit/',
         views.recipe_edit, name='recipe_edit'),
    path('recipes/<int:recipe_id>/<slug:slug>/delete/',
         views.recipe_delete, name='recipe_delete'),
    path('recipes/create/',
         views.recipe_create, name='recipe_create'),
    path('mysubscriptions/',
         views.SubscriptionListView.as_view(), name='subscription_list'),
]
