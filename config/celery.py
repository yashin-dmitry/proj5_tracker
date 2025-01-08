from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Установка переменной окружения для настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создание экземпляра Celery
app = Celery('config')

# Загрузка настройки Celery из Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическая загрузка задач из всех приложений Django
app.autodiscover_tasks()

# Настройка периодической задачи
app.conf.beat_schedule = {
    'send-reminders-every-day': {
        'task': 'habits.tasks.send_reminder',
        'schedule': crontab(minute=0, hour=0),  # Каждый день в полночь
    },
}