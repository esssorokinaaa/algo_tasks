def knapsack_greedy(weights, values, capacity):
    # Создаем список кортежей (вес, ценность) и сортируем по удельной ценности
    items = sorted(zip(weights, values), 
                  key=lambda x: x[1]/x[0],  # Ключ сортировки - ценность/вес
                  reverse=True)             # По убыванию
    
    total_value = 0
    remaining_capacity = capacity
    
    for weight, value in items:
        if remaining_capacity >= weight:
            total_value += value            # Добавляем ценность
            remaining_capacity -= weight    # Уменьшаем оставшийся объем
    
    return total_value
