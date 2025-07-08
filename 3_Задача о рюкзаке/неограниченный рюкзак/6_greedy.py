def unbounded_knapsack_greedy(values, weights, capacity):
    # Создаём список (value, weight, value/weight) и сортируем по убыванию value/weight
    items = sorted(
        [(values[i], weights[i], values[i]/weights[i]) for i in range(len(values))],
        key=lambda x: x[2], reverse=True
    )
    
    total_value = 0
    
    for value, weight, ratio in items:
        if capacity == 0:
            break
        # Сколько раз можем взять этот предмет?
        count = capacity // weight
        total_value += count * value
        capacity -= count * weight
    
    return total_value
