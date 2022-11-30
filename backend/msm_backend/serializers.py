from rest_framework import serializers
from .models import Monster, BreedingCombination


class SimpleMonsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster
        fields = ["id", "name", "elements"]
        depth = 1


class BreedingCombinationSerializer(serializers.ModelSerializer):
    monster_1 = SimpleMonsterSerializer(read_only=True)
    monster_2 = SimpleMonsterSerializer(read_only=True)

    class Meta:
        model = BreedingCombination
        fields = ["monster_1", "monster_2"]


class MonsterImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster
        fields = ["main_image", "egg_image", "portrait_image"]


class CreateMonsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster
        fields = '__all__'


class MonsterSerializer(serializers.ModelSerializer):

    breeding_combinations = BreedingCombinationSerializer(many=True)
    images = serializers.SerializerMethodField()

    def get_images(self, monster):
        return MonsterImageSerializer(instance=monster).data

    def get_breeding_combinations(self, monster):
        print(BreedingCombinationSerializer(read_only=True,
              instance=monster.breeding_combinations).data)
        return BreedingCombinationSerializer(read_only=True, instance=monster.breeding_combinations).data

    class Meta:
        model = Monster
        fields = ["id", "name", "images", "breeding_combinations", "monster_class", "required_beds",
                  "breeding_time", "buying_price", "selling_price", "placement_xp", "islands", "elements", "islands"]
        depth = 1

    # likes_decoration = models.ManyToManyField(to=Decoration,  blank=True)
    # likes_monster = models.ManyToManyField(to="Monster", blank=True)
    # islands = models.ManyToManyField(to=Island)
