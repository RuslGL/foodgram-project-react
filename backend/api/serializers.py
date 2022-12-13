from rest_framework import serializers
from recepies.models import Ingredients, Tags
from users.models import User


from djoser.serializers import UserCreateSerializer, UserSerializer
# from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from users.models import User



# User model serializers

class UserCreateSerializer(UserCreateSerializer):

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
            'password'
        ]

class UserSerializer(UserSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            #'is_subscribed'
        ]


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        exclude = ('id',)


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        exclude = ('id',)
