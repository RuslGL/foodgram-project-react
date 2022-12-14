from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from recepies.models import (Favorite, Ingredients, Recipe, RecipeIngredients,
                             ShoppingCart, Tags)

from .filters import CustomRecipeFilter
from .permissions import IsAuthorAdminOrReadOnly
from .serializers import (CreateRecipeSerializer, FavoriteSerializer,
                          IngredientsSerializer, RecipeSerializer,
                          ShoppingCartSerializer, TagsSerializer,
                          SubscriptionsSerializer, ToSubscribeSerializer)

from users.models import Subscription, User


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
    permission_classes = [AllowAny, ]


class TagsViewSet(viewsets.ModelViewSet):
    """
    Получение списка всех тэгов.
    Права доступа: all users.
    """
    queryset = Tags.objects.all().order_by("id")
    serializer_class = TagsSerializer
    http_method_names = ['get']
    pagination_class = None
    permission_classes = [AllowAny, ]


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


class ShoppingCartView(APIView):
    # только добавить и удалить

    permission_classes = [IsAuthenticated, ]

    def post(self, request, id):
        data = {
            'user': request.user.id,
            'recipe': id
        }
        recipe = get_object_or_404(Recipe, id=id)
        if not ShoppingCart.objects.filter(
           user=request.user, recipe=recipe).exists():
            serializer = ShoppingCartSerializer(
                data=data, context={'request': request}
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
        if ShoppingCart.objects.filter(
           user=request.user, recipe=recipe).exists():
            ShoppingCart.objects.filter(
                user=request.user, recipe=recipe
            ).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def download_shopping_cart(request):

    shopping_list = "Cписок покупок:"
    ingredients = RecipeIngredients.objects.filter(
        recipe__shopping_cart__user=request.user
    ).values(
        'ingredient__name', 'ingredient__measurement_unit'
    ).annotate(amount=Sum('amount'))
    for num, i in enumerate(ingredients):
        shopping_list += (
            f"\n{i['ingredient__name']} - "
            f"{i['amount']} {i['ingredient__measurement_unit']}"
        )
        if num < ingredients.count() - 1:
            shopping_list += ', '
    filename = "shopping_list.txt"
    response = HttpResponse(shopping_list, 'Content-Type: application/txt')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response


class FavoriteView(APIView):

    def post(self, request, id):
        data = {
            'user': request.user.id,
            'recipe': id
        }
        if not Favorite.objects.filter(
           user=request.user, recipe__id=id).exists():
            serializer = FavoriteSerializer(
                data=data, context={'request': request}
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
        if Favorite.objects.filter(
            user=request.user, recipe=recipe
        ).exists():
            Favorite.objects.filter(user=request.user, recipe=recipe).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


###################### Подписки

class ToSubscribeView(APIView):
    def post(self, request, id):
        data = {
            'user': request.user.id,
            'author': id
        }
        serializer = ToSubscribeSerializer(
            data=data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        author = get_object_or_404(User, id=id)
        if Subscription.objects.filter(
           user=request.user, author=author).exists():
            subscription = get_object_or_404(
                Subscription, user=request.user, author=author
            )
            subscription.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class GetSubscriptionsView(ListAPIView):

    def get(self, request):
        user = request.user
        queryset = User.objects.filter(author__user=user)
        page = self.paginate_queryset(queryset)
        serializer = SubscriptionsSerializer(
            page, many=True, context={'request': request}
        )
        return self.get_paginated_response(serializer.data)
