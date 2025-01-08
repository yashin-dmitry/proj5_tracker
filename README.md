# Habit Tracker

## Описание проекта

Habit Tracker — это веб-приложение, которое помогает пользователям отслеживать 
и управлять своими привычками. Приложение позволяет создавать, редактировать 
и удалять привычки, а также напоминать пользователям о выполнении привычек 
через Telegram.

## Используемый стек технологий

- **Backend**: Django, Django REST Framework, Celery
- **Frontend**: React (или другой фронтенд-фреймворк, если используется)
- **Database**: PostgreSQL
- **Message Broker**: Redis
- **Telegram Bot**: python-telegram-bot

## Установка и запуск проекта

### Предварительные требования

- Python 3.8+
- PostgreSQL
- Redis
- Node.js (если используется фронтенд)

### Установка

1. **Клонирование репозитория**

   ```bash
   git clone https://github.com/yashin-dmitry/habbits
   cd habit_tracker

2. **Создание и активация виртуального окружения**   
python -m venv venv
# для Mac: 
source venv/bin/activate
# для Windows: venv\Scripts\activate

1. **Установка зависимостей**
pip install -r requirements.txt

2. **Настройка переменных окружения**

Создайте файл .env в корневой директории проекта и добавьте следующие 
переменные:

DJANGO_SECRET_KEY=your_secret_key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost
DB_NAME=habbits
DB_USER=postgres
DB_PASSWORD=tdpro777
DB_HOST=localhost
DB_PORT=5432
TELEGRAM_BOT_TOKEN=your_telegram_bot_token

5. **Миграции базы данных**
Если база данных еще не настроена, выполните миграции:

python manage.py migrate

6. **Создание суперпользователя**

python manage.py createsuperuser

7. **Запуск Celery Worker и Beat**

celery -A config worker --loglevel=info
celery -A config beat --loglevel=info

8. **Запуск сервера разработки**

python manage.py runserver


Использование:

1) Создание привычки

Откройте браузер и перейдите по адресу http://localhost:8000/admin/. 
Войдите под учетной записью суперпользователя и создайте новую привычку.

2) Получение напоминаний

После создания привычки, вы будете получать напоминания через Telegram 
в указанное время.


Примеры использования:

1) Создание привычки:


{
  "place": "Home",
  "time": "08:00:00",
  "action": "Drink water",
  "is_pleasant": false,
  "periodicity": 1,
  "execution_time": 60,
  "is_public": false
}

2) Получение списка привычек:

GET http://localhost:8000/api/habits/

Документация API:

Документация API доступна по адресу http://localhost:8000/swagger/.

Лицензия:

Этот проект лицензирован под лицензией MIT. Подробнее см. файл LICENSE.

Контакты:

Если у вас есть вопросы или предложения, пожалуйста, свяжитесь с нами:

Email: contact@example.com
GitHub Issues: https://github.com/ваш_пользователь/habit_tracker/issues

