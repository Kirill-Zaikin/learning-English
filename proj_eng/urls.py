"""
URL-конфигурация для проекта `proj_maths`.

Этот модуль содержит маршруты URL, которые связывают запросы с соответствующими представлениями (views) приложения.

Каждый путь (URL) соответствует определенному представлению, которое выполняет соответствующую логику обработки запроса.

Маршруты:
- `''` (home): Главная страница сайта.
- `'terms-list/'`: Страница для отображения списка терминов.
- `'add-term/'`: Страница для добавления нового термина.
- `'send-term/'`: Страница для отправки термина.
- `'stats/'`: Страница для отображения статистики.
- `'texts-list/'`: Страница для отображения списка текстов.
- `'test-input/'`: Страница для ввода тестовых данных.

Функции:
- `path()`: Связывает URL с соответствующим представлением.
- `static()`: Обрабатывает статические файлы.

Для более подробной информации о маршрутизации в Django, см. документацию:
https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('terms-list/', views.terms_list, name='terms_list'),
    path('add-term/', views.add_term, name='add_term'),
    path('send-term/', views.send_term, name='send_term'),
    path('stats/', views.show_stats, name='stats'),
    path('texts-list/', views.texts_list, name='texts_list'),
    path('test-input/',views.test_input, name='test-input')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
