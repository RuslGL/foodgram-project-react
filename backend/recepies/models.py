from django.db import models
# from django.core.validators import MaxValueValidator, MinValueValidator

# from users.models import User


class Ingredients(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        blank=False,
        null=False
        )
    measurement_unit = models.CharField(
        max_length=50,
        blank=False,
        null=False
        )

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        blank=False,
        null=False
        )

    color = models.CharField(
        max_length=7,
        unique=True,
        blank=False,
        null=False
        )

    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.name
