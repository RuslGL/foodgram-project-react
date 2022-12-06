from rest_framework import serializers
from recepies.models import Ingredients, Tags
# from users.models import User


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        exclude = ('id',)


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        exclude = ('id',)
