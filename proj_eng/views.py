"""
Модуль для обработки запросов и отображения данных на сайте с использованием Django.

Этот модуль содержит функции для:
- Отображения списка терминов и текстов.
- Выполнения тестов и отображения результатов.
- Добавления новых терминов.
- Отображения статистики по терминам.

Функции:
    - index: Отображает главную страницу сайта.
    - terms_list: Отображает список терминов.
    - texts_list: Отображает список текстов.
    - test_input: Обрабатывает тестовый запрос и отображает результаты.
    - add_term: Отображает страницу для добавления нового термина.
    - send_term: Обрабатывает добавление нового термина.
    - show_stats: Отображает статистику по терминам.

Используемые модули:
    - terms_work: Модуль для работы с терминами.
    - texts_work: Модуль для работы с текстами.
    - tests_work: Модуль для работы с тестами.

Описание функций:
    index(request):
        Обрабатывает HTTP запрос и рендерит главную страницу сайта.

    terms_list(request):
        Обрабатывает HTTP запрос и рендерит страницу с таблицей терминов.

    texts_list(request):
        Обрабатывает HTTP запрос и рендерит страницу с таблицей текстов.

    test_input(request):
        Обрабатывает запрос для выполнения теста и отображения результатов.

    add_term(request):
        Обрабатывает запрос для отображения страницы добавления нового термина.

    send_term(request):
        Обрабатывает POST запрос для добавления нового термина в систему.

    show_stats(request):
        Обрабатывает запрос и отображает статистику по терминам.
"""

from django.shortcuts import render
from django.core.cache import cache
from . import terms_work
from . import texts_work
from . import tests_work


def index(request):
    """
    Обрабатывает HTTP запрос и рендерит страницу с шаблоном index.html.

    Эта функция:
    - Принимает HTTP запрос от клиента.
    - Использует шаблон "index.html" для генерации HTML-страницы.
    - Возвращает HTTP-ответ с отрендеренной страницей.

    Аргументы:
        request (HttpRequest): Объект запроса, содержащий информацию о запросе от клиента.

    Возвращает:
        HttpResponse: Ответ с отрендеренным шаблоном "index.html".

    Пример:
        index(request)
    """
    return render(request, "index.html")


def terms_list(request):
    """
    Обрабатывает HTTP запрос и рендерит страницу с таблицей терминов.

    Эта функция:
    - Извлекает список терминов с помощью функции `get_terms_for_table` из модуля `terms_work`.
    - Передает полученные данные в шаблон "term_list.html".
    - Возвращает HTTP-ответ с отрендеренной страницей, содержащей таблицу терминов.

    Аргументы:
        request (HttpRequest): Объект запроса, содержащий информацию о запросе от клиента.

    Возвращает:
        HttpResponse: Ответ с отрендеренным шаблоном "term_list.html", включающим данные о терминах.

    Пример:
        terms_list(request)
    """
    terms = terms_work.get_terms_for_table()
    return render(request, "term_list.html", context={"terms": terms})


def texts_list(request):
    """
    Обрабатывает HTTP запрос и рендерит страницу с таблицей текстов.

    Эта функция:
    - Извлекает список текстов с помощью функции `get_texts_for_table` из модуля `texts_work`.
    - Передает полученные данные в шаблон "text_list.html".
    - Возвращает HTTP-ответ с отрендеренной страницей, содержащей таблицу текстов.

    Аргументы:
        request (HttpRequest): Объект запроса, содержащий информацию о запросе от клиента.

    Возвращает:
        HttpResponse: Ответ с отрендеренным шаблоном "text_list.html", включающим данные о текстах.

    Пример:
        texts_list(request)
    """
    texts = texts_work.get_texts_for_table()
    return render(request, "text_list.html", context={"texts": texts})


def test_input(request):
    """
    Обрабатывает HTTP запрос для выполнения теста и отображения результатов.

    Эта функция:
    - Извлекает список тестов с помощью функции `get_tests` из модуля `tests_work`.
    - Если запрос POST, проверяет введенные пользователем ответы и подсчитывает количество правильных ответов.
    - Отправляет результаты (в том числе список данных с ответами и итоговую оценку) в шаблон "test_input_form.html".

    Аргументы:
        request (HttpRequest): Объект запроса, содержащий информацию о запросе от клиента.

    Возвращает:
        HttpResponse: Ответ с отрендеренным шаблоном "test_input_form.html", который либо показывает форму для ввода, либо отображает результаты теста.

    Логика:
        Если запрос GET:
        - Отправляется страница с формой для выполнения теста.
        
        Если запрос POST:
        - Обрабатываются ответы пользователя.
        - Подсчитывается количество правильных ответов и вычисляется итоговый процент.
        - Отправляется страница с результатами теста.

    Пример:
        test_input(request)
    """
    tests = tests_work.get_tests()
    score = None  # Оценка будет по умолчанию None

    if request.method == "POST":
        submitted_data = []
        correct_count = 0
        total_count = len(tests)

        for cnt, text, correct_country in tests:
            user_input = request.POST.get(f"user_input_{cnt}", "").strip()
            is_correct = user_input.lower() == correct_country.lower()
            submitted_data.append((cnt, text, user_input, correct_country, is_correct))

            if is_correct:
                correct_count += 1

        # Подсчитываем процент
        score = (correct_count / total_count) * 100

        return render(request, "test_input_form.html", {
            "submitted_data": submitted_data,
            "score": score
        })

    return render(request, "test_input_form.html", {
        "tests": tests
    })


def add_term(request):
    """
    Обрабатывает HTTP запрос и рендерит страницу для добавления нового термина.

    Эта функция:
    - Принимает запрос от пользователя.
    - Отображает страницу с формой для добавления нового термина.

    Аргументы:
        request (HttpRequest): Объект запроса, содержащий информацию о запросе от клиента.

    Возвращает:
        HttpResponse: Ответ с отрендеренным шаблоном "term_add.html", который содержит форму для добавления термина.

    Пример:
        add_term(request)
    """
    return render(request, "term_add.html")


def send_term(request):
    """
    Обрабатывает POST запрос для отправки нового термина и его описания.

    Эта функция:
    - Принимает данные от пользователя через POST запрос (имя пользователя, новый термин и описание).
    - Проверяет, что термин и описание не пустые.
    - Если данные корректны, добавляет новый термин в список с помощью функции `write_term` из модуля `terms_work`.
    - Отправляет результат (успех или ошибку) обратно пользователю.

    Аргументы:
        request (HttpRequest): Объект запроса, содержащий информацию о запросе от клиента.

    Возвращает:
        HttpResponse: Ответ с отрендеренным шаблоном "term_request.html", который отображает результат добавления термина (успех или ошибку).
        
    Логика:
        Если запрос POST:
        - Проверяются данные для нового термина и его описания.
        - Если данные валидны, термин добавляется.
        - Возвращается страница с результатом добавления.

        Если запрос не POST:
        - Возвращается форма для добавления термина.
    
    Пример:
        send_term(request)
    """
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_term = request.POST.get("new_term", "")
        new_definition = request.POST.get("new_definition", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_definition) == 0:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым"
        elif len(new_term) == 0:
            context["success"] = False
            context["comment"] = "Термин должен быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваше слово добавлено"
            terms_work.write_term(new_term, new_definition)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request.html", context)
    return add_term(request)


def show_stats(request):
    """
    Обрабатывает HTTP запрос и рендерит страницу с статистикой по терминам.

    Эта функция:
    - Извлекает статистику по терминам с помощью функции `get_terms_stats` из модуля `terms_work`.
    - Отправляет полученную статистику в шаблон "stats.html" для отображения пользователю.

    Аргументы:
        request (HttpRequest): Объект запроса, содержащий информацию о запросе от клиента.

    Возвращает:
        HttpResponse: Ответ с отрендеренным шаблоном "stats.html", который содержит статистику по терминам.

    Пример:
        show_stats(request)
    """
    stats = terms_work.get_terms_stats()
    return render(request, "stats.html", stats)
