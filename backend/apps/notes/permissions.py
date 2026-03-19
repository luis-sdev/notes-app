from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Object-level permission: only the note's owner can access it."""

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
