def knapsack_recursive(weights, values, capacity, n):
    # Базовый случай: нет предметов или нет места
    if n == 0 or capacity == 0:
        return 0
    
    # Если вес текущего предмета > вместимости, пропускаем его
    if weights[n-1] > capacity:
        return knapsack_recursive(weights, values, capacity, n-1)
    
    # Возвращаем максимум из двух вариантов:
    # 1. Берем текущий предмет
    # 2. Не берем текущий предмет
    else:
        return max(
            values[n-1] + knapsack_recursive(weights, values, capacity - weights[n-1], n-1),
            knapsack_recursive(weights, values, capacity, n-1)
        )

weights = [1, 2, 3]
values = [10, 15, 40]
capacity = 5
print(knapsack_recursive(weights, values, capacity, len(values)))
