# DPS-MVP-Py
User and resource management for DPS-MVP-Py

# Запуск окружения

### создание окружения

``python -m venv venv``

### скачивание покетов

``pip install -r requirements.txt``

### Создание Django проекта:
``django-admin startproject DAAS``

### надо в settings.py в проекте изменить базу данных

#### на это
``DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DAAS',
        'USER': 'mila',
        'PASSWORD': 'mila',
        'HOST': 'db',
        'PORT': '5432',
    }
}``

### запуск docker оркружения

``docker compose up --build``
