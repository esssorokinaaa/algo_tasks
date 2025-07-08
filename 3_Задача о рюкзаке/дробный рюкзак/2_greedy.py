def fractional_knapsack(values, weights, capacity):
    # Создаем список предметов с дополнительной информацией
    items = []
    for i in range(len(values)):
        items.append({
            'original_index': i,       # Сохраняем исходный индекс
            'value': values[i],
            'weight': weights[i],
            'ratio': values[i] / weights[i]  # Удельная стоимость
        })
    
    # Сортируем по убыванию удельной стоимости
    items.sort(key=lambda x: x['ratio'], reverse=True)
    
    total_value = 0.0
    remaining_capacity = capacity
    selected_items = []  # Для отслеживания взятых предметов
    
    for item in items:
        if remaining_capacity <= 0:
            break
        
        # Определяем сколько взять текущего предмета
        taken_weight = min(item['weight'], remaining_capacity)
        taken_value = taken_weight * item['ratio']
        
        # Записываем сколько взяли
        selected_items.append({
            'index': item['original_index'],
            'weight_taken': taken_weight,
            'value_taken': taken_value
        })
        
        total_value += taken_value
        remaining_capacity -= taken_weight
    
    # Дополнительная информация о выборе
    print("Выбранные предметы:")
    for sel in selected_items:
        print(f"Предмет {sel['index']}: взято {sel['weight_taken']:.2f} кг, стоимость {sel['value_taken']:.2f}")
    
    return total_value
