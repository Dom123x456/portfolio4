# Generated by Django 4.2 on 2023-04-25 23:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MenuItem",
            fields=[
                ("item_id", models.AutoField(primary_key=True, serialize=False)),
                ("item_type", models.IntegerField(choices=[(0, "Food"), (1, "Drink")])),
                ("item_name", models.CharField(max_length=200, unique=True)),
                ("description", models.CharField(max_length=200, unique=True)),
                ("price", models.FloatField()),
                ("dietary", models.CharField(max_length=200)),
                ("allergens", models.CharField(max_length=200, null=True)),
                (
                    "menu_section",
                    models.IntegerField(
                        choices=[
                            (0, "Burgers"),
                            (1, "Sides"),
                            (2, "Desserts"),
                            (3, "Soft Drinks"),
                            (4, "Shakes & Floats"),
                            (5, "Beer"),
                            (6, "Wine & Cocktails"),
                        ]
                    ),
                ),
                ("on_menu", models.BooleanField(default=False)),
                ("updated_on", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["-on_menu"],
            },
        ),
    ]
