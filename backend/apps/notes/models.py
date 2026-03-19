from django.conf import settings
from django.db import models


class Note(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notes",
    )
    title = models.CharField(max_length=255, blank=True, default="")
    body = models.TextField(blank=True, default="")
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="notes",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # auto-stamps on every .save()

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title or "Untitled"
