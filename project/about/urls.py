from about import views
from django.urls import path

urlpatterns = [
    path('author/', views.AboutAuthorView.as_view(), name='author'),
    path('technologies/', views.AboutTechView.as_view(), name='technologies'),
]
