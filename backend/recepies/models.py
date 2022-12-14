from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import UniqueConstraint

from users.models import User


class Ingredients(models.Model):

    name = models.CharField(
        max_length=200,
        unique=True,
        blank=False,
        null=False,
        verbose_name="Наименование"
        )

    measurement_unit = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name="Единицы измеререния"
        )

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"
        ordering = ('name',)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        blank=False,
        null=False,
        verbose_name="Название"
        )

    color = models.CharField(
        max_length=7,
        unique=True,
        blank=False,
        null=False,
        verbose_name="Цвет"
        )

    slug = models.SlugField(
        unique=True,
        verbose_name="Слаг"
        )

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.name


class Recipe(models.Model):

    tags = models.ManyToManyField(
        Tags,
        through='RecipeTags',
        verbose_name='Тэги',
        related_name='tags'
        )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор рецепта'
        )

    ingredients = models.ManyToManyField(
        Ingredients,
        through='RecipeIngredients',
        verbose_name='Ингредиенты'
        )

    image = models.ImageField(
        upload_to='recepies/images/',
        verbose_name="Изображение"
        )

    name = models.CharField(
        max_length=150,
        verbose_name="Название"
        )

    text = models.TextField(
        verbose_name="Описание рецепта"
        )

    cooking_time = models.PositiveIntegerField(
        verbose_name='Время приготовления',
        validators=[MinValueValidator(1)]
        )

    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время публикации рецепта"
        )

    is_favorited = models.ManyToManyField(
        User,
        through='Favorite',
        related_name='favorited_recipes',
        verbose_name='В избранном',
        blank=True
        )

    is_in_shopping_cart = models.ManyToManyField(
        User,
        through='ShoppingCart',
        related_name='recipes_in_cart',
        verbose_name='Рецепты в корзине',
        blank=True
        )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name


class RecipeTags(models.Model):

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )

    tag = models.ForeignKey(
        Tags,
        on_delete=models.CASCADE,
        verbose_name='Тег'
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['recipe', 'tag'],
                name='recipe_tag_unique'
            )
        ]


class RecipeIngredients(models.Model):

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )

    ingredient = models.ForeignKey(
        Ingredients,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент'
    )

    amount = models.IntegerField(
        'Количество',
        validators=[MinValueValidator(1)]
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='recipe_ingredient_unique'
            )
        ]


class ShoppingCart(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='shopping_cart',
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='shopping_cart',
    )

    class Meta:
        verbose_name = 'Корзина покупок'
        verbose_name_plural = 'Корзины пользователей'
        constraints = [
            UniqueConstraint(
                fields=['user', 'recipe'],
                name='user_shoppingcart_unique'
            )
        ]


class Favorite(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='favorites',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='favorites',
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        constraints = [
            UniqueConstraint(
                fields=['user', 'recipe'],
                name='favorite_unique'
            )
        ]
