"""
Конфигурация WSGI для проекта proj_maths.

Этот файл предоставляет переменную уровня модуля с именем ``application``, которая ссылается на WSGI-приложение.

Для получения дополнительной информации о данном файле смотрите
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Устанавливаем переменную окружения, которая указывает Django, какие настройки использовать
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj_eng.settings')

# Создаем WSGI-приложение
application = get_wsgi_application()
