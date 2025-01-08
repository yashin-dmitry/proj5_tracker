import os
import asyncio
from django.core.management.base import BaseCommand
from telegram import Bot

class Command(BaseCommand):
    help = 'Get Telegram chat ID'

    @staticmethod
    async def get_updates():
        bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
        updates = await bot.get_updates()
        for update in updates:
            print(update.message.chat_id)

    def handle(self, *args, **kwargs):
        asyncio.run(self.get_updates())
