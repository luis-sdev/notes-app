from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .models import Category

DEFAULT_CATEGORIES = [
    {"name": "Random Thoughts", "color_hex": "#E8956D"},
    {"name": "Personal", "color_hex": "#7BA7A7"},
    {"name": "School", "color_hex": "#EDD382"},
]


@receiver(post_migrate)
def ensure_default_categories(sender, **kwargs):
    if sender.label != "categories":
        return

    for cat in DEFAULT_CATEGORIES:
        Category.objects.get_or_create(
            name=cat["name"],
            defaults={"color_hex": cat["color_hex"]},
        )
