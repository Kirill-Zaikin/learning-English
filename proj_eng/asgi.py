"""
Конфигурация ASGI для проекта proj_maths.

Этот файл предоставляет объект ASGI, доступный как переменная уровня модуля с именем ``application``.

Для дополнительной информации о данном файле смотрите:
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE для указания настроек проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj_eng.settings')

# Получаем и устанавливаем объект ASGI-приложения
application = get_asgi_application()
