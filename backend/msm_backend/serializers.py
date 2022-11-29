from rest_framework import serializers
from .models import Monster

class MonsterImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster
        fields = ["image", "egg", "portrait"]

class MonsterSerializer(serializers.ModelSerializer):
    images = MonsterImageSerializer(read_only = True,many=True)

    class Meta:
        model = Monster
        fields = ["name","images", "monster_class", "required_beds", "breeding_time", "buying_price", "selling_price","placement_xp", "islands"]
        depth = 1
    
    



    # image
    # egg
    # portrait
    # likes_decoration = models.ManyToManyField(to=Decoration,  blank=True)
    # likes_monster = models.ManyToManyField(to="Monster", blank=True)
    # elements = models.ManyToManyField(to="Element", blank=True)
    # islands = models.ManyToManyField(to=Island)
