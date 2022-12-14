from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (FavoriteView, IngredientsViewSet, RecipeViewSet,
                    ShoppingCartView, TagsViewSet, download_shopping_cart, 
                    ToSubscribeView, GetSubscriptionsView)

app_name = 'api'

router = DefaultRouter()

router.register('ingredients', IngredientsViewSet, basename='ingredients')
router.register('tags', TagsViewSet, basename='tags')
router.register('recipes', RecipeViewSet, basename='recipes')

urlpatterns = [
    path(
        'users/<int:id>/subscribe/',
        ToSubscribeView.as_view(),
        name='subscribe'
    ),
    path(
        'users/subscriptions/',
        GetSubscriptionsView.as_view(),
        name='subscriptions'
    ),
    path(
        'recipes/<int:id>/favorite/',
        FavoriteView.as_view(),
        name='favorite'
    ),
    path(
        'recipes/download_shopping_cart/',
        download_shopping_cart,
        name='download_shopping_cart'
    ),
    path(
        'recipes/<int:id>/shopping_cart/',
        ShoppingCartView.as_view(),
        name='shopping_cart'
    ),


    path('auth/', include('djoser.urls.authtoken')),
    path('', include('djoser.urls')),
    path('', include(router.urls)),
]
