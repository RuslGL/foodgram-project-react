from django_filters import rest_framework as filter

from recepies.models import Recipe, Tags


class CustomRecipeFilter(filter.FilterSet):

    is_favorited = filter.BooleanFilter(method='is_favorited')

    author = filter.CharFilter()

    is_in_shopping_cart = filter.BooleanFilter(
        method='is_in_shopping_cart')

    tags = filter.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        queryset=Tags.objects.all(),
        label='Tags',
        to_field_name='slug'
    )

    class Meta:
        model = Recipe
        fields = ['is_favorited', 'author', 'is_in_shopping_cart',  'tags', ]

    def is_favorited(self, queryset, name, value):
        if value:
            return queryset.filter(favorites__user=self.request.user)
        return queryset

    def is_in_shopping_cart(self, queryset, name, value):
        if value:
            return queryset.filter(shopping_cart__user=self.request.user)
        return queryset
