# from django.contrib.auth.tokens import default_token_generator
# from django.shortcuts import get_object_or_404
from rest_framework import generics, filters, mixins, viewsets, status
# from rest_framework.decorators import action, api_view, permission_classes
# from rest_framework.throttling import AnonRateThrottle
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.permissions import (AllowAny, IsAuthenticated,
#                                        IsAuthenticatedOrReadOnly)
# from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.core.mail import send_mail
# from django.db.models import Avg
# from django_filters.rest_framework import DjangoFilterBackend

from recepies.models import Ingredients, Tags
#from api_yamdb.settings import EMAIL_BACKEND
#from users.models import User
from .serializers import IngredientsSerializer, TagsSerializer


class IngredientsViewSet(viewsets.ModelViewSet):
    """
    Получение списка всех ингридиентов.
    Права доступа: ______________.
    """
    queryset = Ingredients.objects.all().order_by("id")
    serializer_class = IngredientsSerializer
    http_method_names = ['get']


class TagsViewSet(viewsets.ModelViewSet):
    """
    Получение списка всех тэгов.
    Права доступа: ______________.
    """
    queryset = Tags.objects.all().order_by("id")
    serializer_class = TagsSerializer
    http_method_names = ['get']
