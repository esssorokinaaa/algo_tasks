def unbounded_knapsack_dp(values, weights, capacity):
    n = len(values)
    dp = [0] * (capacity + 1)  # dp[w] = макс. стоимость для веса w
    
    for w in range(1, capacity + 1):  # Перебираем все возможные веса
        for i in range(n):  # Проверяем все предметы
            if weights[i] <= w:  # Если предмет помещается
                # Выбираем максимум: не брать или взять предмет
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]
