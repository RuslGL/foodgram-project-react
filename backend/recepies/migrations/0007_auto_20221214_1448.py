# Generated by Django 2.2.16 on 2022-12-14 11:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepies', '0006_auto_20221214_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='is_favorited',
            field=models.ManyToManyField(blank=True, related_name='favorited_recipes', through='recepies.Favorite', to=settings.AUTH_USER_MODEL, verbose_name='В избранном'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='is_in_shopping_cart',
            field=models.ManyToManyField(blank=True, related_name='recipes_in_cart', through='recepies.ShoppingCart', to=settings.AUTH_USER_MODEL, verbose_name='Рецепты в корзине'),
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]
