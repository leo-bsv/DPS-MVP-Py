# DPS-MVP-Py
User and resource management for DPS-MVP-Py

# Запуск окружения

### создание окружения

``python3 -m venv venv``

### вход в окружение

``source venv/bin/activate``

### скачивание покетов

``pip install -r requirements.txt``

### создание docker оркружения

``make start``

### для остановки всех контейнеров

``make stop``

### для вывода логов контейнеров использовать

``logs_web, logs_nginx, logs_psql, logs``

### создать миграцию
``make makemigrations ``

### выполнить миграции 
`` make migrate ``

### для запуска с логами ли без

``run_logs, run``

### для написания команд в докер к серверу сайта

``make input command=(команда которую надо уже после python manage)``
