from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Класс разрешений для проверки доступа к объектам.

    Attributes:
        has_object_permission (method): Метод для проверки доступа к объекту.
    """
    def has_object_permission(self, request, view, obj):
        """
        Проверяет, имеет ли пользователь разрешение на выполнение операции
        над объектом.

        Args:
            request (Request): Объект запроса.
            view (View): Объект представления.
            obj (Habit): Объект модели Habit.

        Returns:
            bool: True, если пользователь имеет разрешение, иначе False.
        """
        # Разрешения на чтение доступны всем пользователям.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешения на запись доступны только владельцу объекта.
        return obj.user == request.user
