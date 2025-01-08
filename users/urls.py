from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, RegisterView, LoginView

# Создаем маршрутизатор
router = DefaultRouter()

# Регистрируем ViewSet для пользователей
router.register(r'users', CustomUserViewSet)

# URL-конфигурация
urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
