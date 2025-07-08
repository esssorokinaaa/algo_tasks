def knapsack_dp(weights, values, capacity):
    n = len(values)
    # Создаем таблицу (n+1) x (capacity+1), инициализированную нулями
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):          # Перебираем предметы
        for w in range(1, capacity + 1): # Перебираем все возможные веса
            if weights[i-1] <= w:
                # Максимум из вариантов - взять или не взять текущий предмет
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]], 
                    dp[i-1][w]
                )
            else:
                # Если предмет не влезает - используем предыдущий результат
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]  # Правый нижний элемент - ответ
