from django.apps import AppConfig


class CategoriesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.categories"

    def ready(self):
        # Register signal handlers (post_migrate default category seed).
        from . import signals  # noqa: F401
