from rest_framework import permissions


# Allows read-only access to everyone and write access only to the object owner
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Safe methods are GET/HEAD/OPTIONS which won't affect database objects and are read-only
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_name == request.user
