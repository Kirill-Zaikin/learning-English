def get_terms_for_table():
    """
    Читает данные из CSV файла с терминами и их определениями и возвращает список строк в формате таблицы.

    Ожидается, что файл CSV имеет следующую структуру:
    - Каждая строка содержит термин, его определение и источник, разделенные точкой с запятой.
    - Первая строка в файле должна быть заголовком и игнорируется.

    Возвращает:
        list: Список списков, где каждый элемент содержит:
            - Номер строки в таблице (начиная с 1)
            - Термин
            - Определение термина

    Пример возвращаемого значения:
        [
            [1, 'Term1', 'Definition of term 1'],
            [2, 'Term2', 'Definition of term 2'],
            ...
        ]
    """
    terms = []
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            term, definition, source = line.split(";")
            terms.append([cnt, term, definition])
            cnt += 1
    return terms



def write_term(new_term, new_definition):
    """
    Добавляет новый термин и его определение в файл CSV, сортируя термины в алфавитном порядке.

    Эта функция:
    - Считывает существующие термины из файла CSV.
    - Добавляет новый термин и его определение в файл.
    - Сортирует все термины в алфавитном порядке.
    - Перезаписывает файл с обновленным списком терминов.

    Аргументы:
        new_term (str): Новый термин, который будет добавлен в файл.
        new_definition (str): Определение для нового термина.

    Возвращает:
        None: Функция не возвращает значения, а выполняет операцию записи в файл.
    
    Пример:
        write_term("new_term", "This is a new term's definition.")
    """
    new_term_line = f"{new_term};{new_definition};user"
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        existing_terms = [l.strip("\n") for l in f.readlines()]
        title = existing_terms[0]
        old_terms = existing_terms[1:]
    
    terms_sorted = old_terms + [new_term_line]
    terms_sorted.sort()
    new_terms = [title] + terms_sorted
    
    with open("./data/terms.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_terms))



def get_terms_stats():
    """
    Рассчитывает статистику по терминам и их определениям из файла CSV.

    Эта функция:
    - Подсчитывает общее количество терминов, добавленных пользователями и из базы данных.
    - Рассчитывает среднее количество слов в определении, максимальную и минимальную длину определения (в словах).
    - Возвращает словарь с полученной статистикой.

    Возвращает:
        dict: Словарь с ключами:
            - "terms_all": Общее количество терминов (пользовательских и из базы данных).
            - "terms_own": Количество терминов, добавленных из базы данных.
            - "terms_added": Количество терминов, добавленных пользователями.
            - "words_avg": Среднее количество слов в определениях.
            - "words_max": Максимальное количество слов в определении.
            - "words_min": Минимальное количество слов в определении.

    Пример возвращаемого значения:
        {
            "terms_all": 100,
            "terms_own": 80,
            "terms_added": 20,
            "words_avg": 15.2,
            "words_max": 30,
            "words_min": 5
        }
    """
    db_terms = 0
    user_terms = 0
    defin_len = []
    
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            term, defin, added_by = line.split(";")
            words = defin.split()
            defin_len.append(len(words))
            if "user" in added_by:
                user_terms += 1
            elif "db" in added_by:
                db_terms += 1
    
    stats = {
        "terms_all": db_terms + user_terms,
        "terms_own": db_terms,
        "terms_added": user_terms,
        "words_avg": sum(defin_len)/len(defin_len),
        "words_max": max(defin_len),
        "words_min": min(defin_len)
    }
    
    return 
