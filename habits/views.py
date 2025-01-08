from rest_framework import viewsets, permissions, generics
from .models import Habit
from .serializers import HabitSerializer
from .permissions import IsOwnerOrReadOnly

class HabitViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели Habit.

    Attributes:
        queryset (QuerySet): Набор объектов модели Habit.
        serializer_class (HabitSerializer): Класс сериализатора для модели
        Habit.
        permission_classes (list): Список классов разрешений.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        """
        Возвращает набор объектов модели Habit для текущего пользователя.

        Returns:
            QuerySet: Набор объектов модели Habit для текущего пользователя.
        """
        if self.request.user.is_authenticated:
            return Habit.objects.filter(user=self.request.user)
        return Habit.objects.none()

    def perform_create(self, serializer):
        """
        Сохраняет новый объект модели Habit с текущим пользователем.

        Args:
            serializer (HabitSerializer): Сериализатор для модели Habit.
        """
        serializer.save(user=self.request.user)

class PublicHabitListView(generics.ListAPIView):
    """
    View для отображения списка публичных привычек.

    Attributes:
        queryset (QuerySet): Набор объектов модели Habit, которые являются
        публичными.
        serializer_class (HabitSerializer): Класс сериализатора для модели
        Habit.
        permission_classes (list): Список классов разрешений.
    """
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    permission_classes = [permissions.AllowAny]
