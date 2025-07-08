def fractional_knapsack_dp(values, weights, capacity):
    n = len(values)
    dp = [0.0] * (capacity + 1)
    decisions = [[] for _ in range(capacity + 1)]  # Для отслеживания выбора
    
    for w in range(1, capacity + 1):
        max_val = 0.0
        best_decision = []
        
        for i in range(n):
            if weights[i] <= w:
                # Вариант 1: взять целый предмет
                candidate_val = dp[w - weights[i]] + values[i]
                if candidate_val > max_val:
                    max_val = candidate_val
                    best_decision = decisions[w - weights[i]] + [(i, 1.0)]  # 1.0 - целый предмет
            else:
                # Вариант 2: взять часть предмета
                fraction = w / weights[i]
                candidate_val = fraction * values[i]
                if candidate_val > max_val:
                    max_val = candidate_val
                    best_decision = [(i, fraction)]
        
        dp[w] = max_val
        decisions[w] = best_decision
    
    # Выводим информацию о выборе
    print("Выбранные предметы для capacity =", capacity)
    for item, fraction in decisions[capacity]:
        print(f"Предмет {item}: взято {fraction*100:.1f}% (вес {weights[item]*fraction:.1f}, стоимость {values[item]*fraction:.1f})")
    
    return dp[capacity]
