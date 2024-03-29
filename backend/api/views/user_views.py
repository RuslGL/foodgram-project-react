from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Subscription, User

from ..serializers import SubscriptionsSerializer, ToSubscribeSerializer


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
        queryset = User.objects.filter(
            author__user=user).annotate(Count('recipes'))
        page = self.paginate_queryset(queryset)
        serializer = SubscriptionsSerializer(
            page, many=True,
            context={'request': request, "queryset": queryset}
        )
        return self.get_paginated_response(serializer.data)
