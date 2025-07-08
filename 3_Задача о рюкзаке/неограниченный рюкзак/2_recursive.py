def unbounded_knapsack_recursive(values, weights, capacity, n):
    
    # Базовый случай: если вместимость = 0 или предметы кончились
    if capacity == 0 or n == 0:
        return 0
    
    # Если текущий предмет не помещается, пропускаем его
    if weights[n-1] > capacity:
        result = unbounded_knapsack_recursive(values, weights, capacity, n-1)
    else:
        # Вариант 1: берём текущий предмет (можем взять снова)
        take = values[n-1] + unbounded_knapsack_recursive(values, weights, capacity - weights[n-1], n)
        # Вариант 2: не берём текущий предмет (переходим к следующему)
        not_take = unbounded_knapsack_recursive(values, weights, capacity, n-1)
        # Выбираем максимум из двух вариантов
        result = max(take, not_take)
    
    return result
