# applications/permissions.py
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Allow only the owner of the object to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
