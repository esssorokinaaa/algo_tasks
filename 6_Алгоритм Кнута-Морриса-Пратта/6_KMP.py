def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m  # Инициализируем массив нулями
    length = 0      # Длина текущего longest prefix suffix
    i = 1           # Индекс для перемещения по образцу
    
    while i < m:
        if pattern[i] == pattern[length]:
            # Если символы совпадают, увеличиваем длину
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # Возвращаемся к предыдущему longest prefix
                length = lps[length-1]
            else:
                # Нет совпадений - записываем 0 и двигаемся дальше
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    result = []
    i = 0  # Индекс для текста
    j = 0  # Индекс для образца
    
    while i < n:
        if text[i] == pattern[j]:
            # Символы совпали - двигаемся дальше
            i += 1
            j += 1
            
            if j == m:
                # Нашли полное совпадение
                result.append(i-j)
                # Используем lps для поиска возможных перекрытий
                j = lps[j-1]
        else:
            if j != 0:
                # Используем lps для "перепрыгивания"
                j = lps[j-1]
            else:
                # Первый символ не совпал - просто двигаемся по тексту
                i += 1
    return result
