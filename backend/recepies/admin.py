from django.contrib import admin

from .models import Ingredients, Tags


@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit',)
    empty_value_display: str = '-пусто-'


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'slug',)
    empty_value_display: str = '-пусто-'
