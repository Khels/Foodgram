from django.urls import include, path
from rest_framework.routers import DefaultRouter, Route, SimpleRouter

from . import views


class CustomReadOnlyRouter(SimpleRouter):
    """
    A router for read-only APIs, which doesn't use trailing slashes.
    """
    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
    ]


custom_router = CustomReadOnlyRouter()
custom_router.register(
    r'ingredients', views.IngredientViewset, basename='ingredients'
)

urlpatterns = [
    path('v1/', include(custom_router.urls)),
    path('v1/subscriptions/', views.FollowView.as_view()),
    path('v1/subscriptions/<int:id>/', views.FollowView.as_view()),
]
