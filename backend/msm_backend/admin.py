from django.contrib import admin
from .models import Monster, BreedingCombination, Decoration, Element, MaxAmount, Earning, FeedingCost, Island, MonsterClass


@admin.register(Monster)
class MonsterAdmin(admin.ModelAdmin):
    list_display = ["name", "main_image", "portrait_image"]


@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = ["name", "image"]


@admin.register(BreedingCombination)
class BreedingCombinationAdmin(admin.ModelAdmin):
    list_display = ["monster", "monster_1", "monster_2"]


@admin.register(Decoration)
class DecorationAdmin(admin.ModelAdmin):
    list_display = ["name", "image"]


@admin.register(MaxAmount)
class MaxAmountAdmin(admin.ModelAdmin):
    list_display = ["monster", "level", "amount"]


@admin.register(Earning)
class EarningAdmin(admin.ModelAdmin):
    list_display = ["monster", "level", "earning"]


@admin.register(FeedingCost)
class FeedingCostAdmin(admin.ModelAdmin):
    list_display = ["monster", "level", "cost"]


@admin.register(Island)
class IslandAdmin(admin.ModelAdmin):
    list_display = ["name", "image"]


@admin.register(MonsterClass)
class MonsterClassAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
