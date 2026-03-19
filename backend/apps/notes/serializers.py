from rest_framework import serializers
from apps.categories.serializers import CategorySerializer
from apps.categories.models import Category
from .models import Note


class NoteListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for dashboard note cards.
    Returns raw ISO datetimes — all formatting is handled by the frontend.
    """
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True,
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Note
        fields = ["id", "title", "body", "category", "category_id", "updated_at"]


class NoteDetailSerializer(serializers.ModelSerializer):
    """Full serializer for the note editor modal.
    Returns raw ISO datetimes — all formatting is handled by the frontend.
    """
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True,
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Note
        fields = ["id", "title", "body", "category", "category_id", "created_at", "updated_at"]
