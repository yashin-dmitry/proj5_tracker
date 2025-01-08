from celery import shared_task
from telegram import Bot
from .models import Habit
import os

@shared_task
def send_reminder():
    """
    Отправляет напоминания пользователям о выполнении привычек.

    Эта задача выполняется ежедневно в полночь и отправляет сообщения
    пользователям через Telegram.
    """
    bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
    habits = Habit.objects.all()
    for habit in habits:
        message = f"Напоминание: {habit.action} в {habit.time} в {habit.place}"
        bot.send_message(chat_id=habit.user.telegram_chat_id, text=message)
