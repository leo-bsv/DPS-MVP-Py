# DPS-MVP-Py
User and resource management for DPS-MVP-Py

# Запуск окружения

### создание окружения

``make start``

### для прокидывания портов

``sudo nano /etc/hosts``
#### и в конец вставте

``127.0.0.1 daas-mvp.com``

### создание docker оркружения

``make build_env``

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
