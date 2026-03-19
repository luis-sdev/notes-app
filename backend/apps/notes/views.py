from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Note
from .permissions import IsOwner
from .serializers import NoteListSerializer, NoteDetailSerializer


class NoteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    def get_queryset(self):
        qs = Note.objects.filter(user=self.request.user).select_related("category")
        category_id = self.request.query_params.get("category")
        if category_id:
            qs = qs.filter(category_id=category_id)
        return qs

    def get_serializer_class(self):
        # List → lightweight card serializer; all other actions → full detail serializer
        if self.action == "list":
            return NoteListSerializer
        return NoteDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
