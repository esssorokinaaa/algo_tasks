def dp_coin_change(coins, amount):
    # Инициализация: dp[0] = 0, остальные - "бесконечность"
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    # Также можно сохранять, какие монеты использовались
    coin_used = [-1] * (amount + 1)
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    # Восстановление решения
    if dp[amount] == float('inf'):
        return -1, []
    
    # Собираем использованные монеты
    result = []
    remaining = amount
    while remaining > 0:
        coin = coin_used[remaining]
        result.append(coin)
        remaining -= coin
    
    return dp[amount], result
