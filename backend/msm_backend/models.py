from django.db import models

class Decoration(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/decorations")

    def __str__(self) -> str:
        return self.name

class Element(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/elements")

    def __str__(self) -> str:
        return self.name

class MonsterClass(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class Island(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/islands")

    def __str__(self) -> str:
        return self.name

class Monster(models.Model):
    name = models.CharField(max_length=255)
    likes_decoration = models.ManyToManyField(to=Decoration,  blank=True)
    likes_monster = models.ManyToManyField(to="Monster", blank=True)
    image = models.ImageField(upload_to="images/monsters/main")
    elements = models.ManyToManyField(to="Element", blank=True)
    monster_class = models.ForeignKey(MonsterClass, on_delete=models.PROTECT, null=True)
    egg = models.ImageField(upload_to="images/monsters/eggs")
    portrait = models.ImageField(upload_to="images/monsters/portraits")
    islands = models.ManyToManyField(to=Island)
    required_beds = models.PositiveSmallIntegerField()
    breeding_time = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    buying_price = models.PositiveSmallIntegerField()
    selling_price = models.PositiveIntegerField()
    placement_xp = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ["name"]

class Earning(models.Model):
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField()
    earning = models.PositiveIntegerField()

    class Meta:
        unique_together = ("monster", "level")

class MaxAmount(models.Model):
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField()
    amount = models.PositiveIntegerField()

    class Meta:
        ordering = ["monster__name", "level"]
        unique_together = ("monster", "level")

class BreedingCombination(models.Model):
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE, related_name="breeding_combination")
    monster_1 = models.ForeignKey(Monster, on_delete=models.CASCADE, related_name="+")
    monster_2 = models.ForeignKey(Monster, on_delete=models.CASCADE, related_name="+")

class FeedingCost(models.Model):
    monster = models.ForeignKey("Monster", on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField()
    cost = models.PositiveIntegerField()

    class Meta:
        ordering = ["monster__name", "cost"]
        unique_together = ("monster", "level")