def boyer_moore_search(text, pattern):
  
    def build_bad_char_table(pattern):
        """
        Создаем таблицу 'плохих символов'
        Для каждого символа в образце хранится его последняя позиция.
        Если символ не встречается в образце, используется длина образца.
        """
        table = {}
        length = len(pattern)
        for i in range(length - 1):  # Не учитываем последний символ
            table[pattern[i]] = length - i - 1
        return table

    def build_good_suffix_table(pattern):
        """
        Создаем таблицу 'хороших суффиксов'
        Определяем, насколько можно сдвинуть образец при несовпадении,
        учитывая уже совпавшие суффиксы.
        """
        length = len(pattern)
        table = [0] * length
        last_prefix = length  # Позиция начала префикса

        # Первый проход: ищем префиксы
        for i in range(length - 1, -1, -1):
            if is_prefix(pattern, i + 1):
                last_prefix = i + 1
            table[i] = last_prefix + (length - 1 - i)

        # Второй проход: ищем суффиксы
        for i in range(length - 1):
            slen = suffix_length(pattern, i)
            if pattern[i - slen] != pattern[length - 1 - slen]:
                table[slen] = length - 1 - i + slen

        return table

    def is_prefix(pattern, p):
        """
        Проверяем, является ли подстрока pattern[p:] префиксом pattern.
        """
        for i in range(p, len(pattern)):
            if pattern[i] != pattern[i - p]:
                return False
        return True

    def suffix_length(pattern, p):
        """
        Возвращаем длину максимального суффикса, который совпадает
        с окончанием pattern[p+1:].
        """
        length = len(pattern)
        slen = 0
        while (p - slen >= 0 and 
               pattern[p - slen] == pattern[length - 1 - slen]):
            slen += 1
        return slen

    # Основное тело функции поиска
    if not pattern:  # Пустой образец
        return []

    n = len(text)
    m = len(pattern)
    result = []

    # Предварительная обработка образца
    bad_char = build_bad_char_table(pattern)
    good_suffix = build_good_suffix_table(pattern)

    i = 0  # Текущая позиция в тексте
    while i <= n - m:
        j = m - 1  # Начинаем сравнение с конца образца

        # Сравниваем справа налево
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            # Найдено полное совпадение
            result.append(i)
            # Сдвигаем по правилу хорошего суффикса
            i += good_suffix[0] if m > 1 else 1
        else:
            # Вычисляем сдвиг по правилу плохого символа
            char = text[i + j]
            bc_shift = bad_char.get(char, m) - (m - 1 - j)
            
            # Вычисляем сдвиг по правилу хорошего суффикса
            gs_shift = good_suffix[j]
            
            # Выбираем максимальный сдвиг (но не меньше 1)
            i += max(bc_shift, gs_shift, 1)

    return result
