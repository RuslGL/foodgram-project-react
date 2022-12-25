from django_filters import rest_framework as filter
from rest_framework.filters import SearchFilter

from recepies.models import Recipe


class IngredientFilter(SearchFilter):
    search_param = 'name'


class CustomRecipeFilter(filter.FilterSet):

    tags = filter.CharFilter(
        field_name='tags__slug', lookup_expr='icontains')
    is_favorited = filter.BooleanFilter(method='get_is_favorited')
    is_in_shopping_cart = filter.BooleanFilter(
        method='get_is_in_shopping_cart'
    )

    class Meta:
        model = Recipe
        fields = ['tags', 'author', 'is_favorited', 'is_in_shopping_cart']

    def get_is_favorited(self, queryset, name, value):
        user = self.request.user
        if value and user.is_authenticated:
            return queryset.filter(favorites__user=user)
        return queryset

    def get_is_in_shopping_cart(self, queryset, name, value):
        user = self.request.user
        if value and user.is_authenticated:
            return queryset.filter(shopping_cart__user=user)
        return queryset
