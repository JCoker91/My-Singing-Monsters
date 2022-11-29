# Generated by Django 4.1.3 on 2022-11-29 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Decoration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to="images/decorations")),
            ],
        ),
        migrations.CreateModel(
            name="Element",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to="images/elements")),
            ],
        ),
        migrations.CreateModel(
            name="Island",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to="images/islands")),
            ],
        ),
        migrations.CreateModel(
            name="MonsterClass",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Monster",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to="images/monsters/main")),
                ("egg", models.ImageField(upload_to="images/monsters/eggs")),
                ("portrait", models.ImageField(upload_to="images/monsters/portraits")),
                ("required_beds", models.PositiveSmallIntegerField()),
                (
                    "breeding_time",
                    models.DecimalField(decimal_places=2, default=0, max_digits=6),
                ),
                ("buying_price", models.PositiveSmallIntegerField()),
                ("selling_price", models.PositiveIntegerField()),
                ("placement_xp", models.PositiveIntegerField()),
                (
                    "elements",
                    models.ManyToManyField(blank=True, to="msm_backend.element"),
                ),
                ("islands", models.ManyToManyField(to="msm_backend.island")),
                (
                    "likes_decoration",
                    models.ManyToManyField(blank=True, to="msm_backend.decoration"),
                ),
                (
                    "likes_monster",
                    models.ManyToManyField(blank=True, to="msm_backend.monster"),
                ),
                (
                    "monster_class",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="msm_backend.monsterclass",
                    ),
                ),
            ],
            options={"ordering": ["name"],},
        ),
        migrations.CreateModel(
            name="MaxAmount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("level", models.PositiveSmallIntegerField()),
                ("amount", models.PositiveIntegerField()),
                (
                    "monster",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="msm_backend.monster",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FeedingCost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("level", models.PositiveSmallIntegerField()),
                ("cost", models.PositiveIntegerField()),
                (
                    "monster",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="msm_backend.monster",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Earning",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("level", models.PositiveSmallIntegerField()),
                ("earning", models.PositiveIntegerField()),
                (
                    "monster",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="msm_backend.monster",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BreedingCombination",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "monster",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="breeding_combination",
                        to="msm_backend.monster",
                    ),
                ),
                (
                    "monster_1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="msm_backend.monster",
                    ),
                ),
                (
                    "monster_2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="msm_backend.monster",
                    ),
                ),
            ],
        ),
    ]