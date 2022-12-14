from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from recepies.models import Ingredients, Recipe, Tags

from ..filters import CustomRecipeFilter
from ..permissions import IsAuthorAdminOrReadOnly
from ..serializers import (CreateRecipeSerializer, IngredientsSerializer,
                           RecipeSerializer, TagsSerializer)


class IngredientsViewSet(viewsets.ModelViewSet):
    """
    Получение списка всех ингридиентов.
    Права доступа: all users.
    """
    queryset = Ingredients.objects.all().order_by("id")
    serializer_class = IngredientsSerializer
    http_method_names = ['get']
    pagination_class = None
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name',)


class TagsViewSet(viewsets.ModelViewSet):
    """
    Получение списка всех тэгов.
    Права доступа: all users.
    """
    queryset = Tags.objects.all().order_by("id")
    serializer_class = TagsSerializer
    http_method_names = ['get']
    pagination_class = None


class RecipeViewSet(viewsets.ModelViewSet):

    queryset = Recipe.objects.all()
    permission_classes = [IsAuthorAdminOrReadOnly, ]
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = CustomRecipeFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RecipeSerializer
        return CreateRecipeSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context