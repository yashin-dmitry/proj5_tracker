# Используем официальный образ PostgreSQL
FROM postgres:13

# Устанавливаем рабочую директорию
WORKDIR /var/lib/postgresql/data

# Копируем файл .env
COPY .env /var/lib/postgresql/data/.env

# Открываем порт 5432
EXPOSE 5432
