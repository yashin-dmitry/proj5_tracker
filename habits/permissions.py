from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешения на чтение доступны всем пользователям.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешения на запись доступны только владельцу объекта.
        return obj.user == request.user
