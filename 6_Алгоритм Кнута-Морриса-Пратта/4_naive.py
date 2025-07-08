def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    result = []  # Здесь будем хранить индексы вхождений
    
    # Перебираем все возможные стартовые позиции в тексте
    for i in range(n - m + 1):
        j = 0  # Индекс для перемещения по образцу
        
        # Пока символы совпадают и не дошли до конца образца
        while j < m and text[i+j] == pattern[j]:
            j += 1
        
        # Если дошли до конца образца - значит, нашли совпадение
        if j == m:
            result.append(i)  # Запоминаем позицию
    
    return result
