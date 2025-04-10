#!/usr/bin/env python
"""Утилита командной строки Django для административных задач."""
import os
import sys

def main():
    """Выполнение административных задач."""
    # Устанавливаем переменную окружения, которая указывает Django, какие настройки использовать
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj_eng.settings')

    try:
        # Пытаемся импортировать функцию для выполнения команд Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Если импорт не удался, выбрасываем исключение с пояснением
        raise ImportError(
            "Не удалось импортировать Django. Убедитесь, что он установлен и "
            "доступен в вашем PYTHONPATH? Вы не забыли активировать виртуальное окружение?"
        ) from exc
    
    # Выполняем команду, переданную в командной строке
    execute_from_command_line(sys.argv)

# Запускаем функцию main, если этот файл был вызван напрямую
if __name__ == '__main__':
    main()
