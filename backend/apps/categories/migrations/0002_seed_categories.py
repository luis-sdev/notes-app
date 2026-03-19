from django.db import migrations

CATEGORIES = [
    {"name": "Random Thoughts", "color_hex": "#E8956D"},
    {"name": "Personal", "color_hex": "#7BA7A7"},
    {"name": "School", "color_hex": "#EDD382"},
]


def seed_categories(apps, schema_editor):
    Category = apps.get_model("categories", "Category")
    for cat in CATEGORIES:
        Category.objects.get_or_create(name=cat["name"], defaults={"color_hex": cat["color_hex"]})


def unseed_categories(apps, schema_editor):
    Category = apps.get_model("categories", "Category")
    Category.objects.filter(name__in=[c["name"] for c in CATEGORIES]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_categories, reverse_code=unseed_categories),
    ]
