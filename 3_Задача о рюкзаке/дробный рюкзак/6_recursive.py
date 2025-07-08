def fractional_knapsack_recursive(values, weights, capacity, index=0):
    
    # Базовые случаи
    if capacity <= 0 or index >= len(values):
        return 0.0
    
    current_value = values[index]
    current_weight = weights[index]
    
    # Случай 1: не берем текущий предмет
    max_value = fractional_knapsack_recursive(values, weights, capacity, index + 1)
    
    if current_weight <= capacity:
        # Случай 2: берем целый предмет
        val_with = current_value + fractional_knapsack_recursive(values, weights, capacity - current_weight, index)
        max_value = max(max_value, val_with)
    else:
        # Случай 3: берем часть предмета
        fraction = capacity / current_weight
        val_part = fraction * current_value
        max_value = max(max_value, val_part)
    
    return max_value
