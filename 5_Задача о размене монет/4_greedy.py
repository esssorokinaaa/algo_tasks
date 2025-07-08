def greedy_coin_change(coins, amount):
    # Сортируем монеты по убыванию для жадного выбора
    coins.sort(reverse=True)
    result = []
    
    for coin in coins:
        # Пока текущая монета не больше оставшейся суммы
        while amount >= coin:
            amount -= coin
            result.append(coin)
    
    # Если удалось полностью разменять сумму
    if amount == 0:
        return result
    else:
        return None  # Решение не найдено
