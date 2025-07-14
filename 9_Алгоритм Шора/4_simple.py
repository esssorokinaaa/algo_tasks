import math
import random
from fractions import Fraction

def shor_algorithm(N):
    """Основная функция алгоритма Шора для факторизации числа N"""
    
    # 1. Проверка простых случаев
    if N % 2 == 0:
        return 2
    if is_power(N):
        return is_power(N)
    
    # 2. Подготовка случайного основания
    while True:
        a = random.randint(2, N-1)
        gcd = math.gcd(a, N)
        if gcd != 1:
            return gcd
        
        # 3. Упрощённый вариант квантовой части (поиск периода)
        r = find_period_classically(a, N)
        
        # 4. Если период найден и он четный
        if r is not None and r % 2 == 0:
            # Вычисляем потенциальные множители
            factor1 = math.gcd(a**(r//2) - 1, N)
            factor2 = math.gcd(a**(r//2) + 1, N)
            
            if factor1 not in [1, N] and N % factor1 == 0:
                return factor1
            if factor2 not in [1, N] and N % factor2 == 0:
                return factor2

def find_period_classically(a, N):
    """Упрощение квантовой части для поиска периода"""
    # Ищем наименьшее r, где a^r ≡ 1 mod N
    for r in range(1, N):
        if pow(a, r, N) == 1:
            return r
    return None

def is_power(n):
    """Проверяем, является ли число степенью другого числа"""
    for b in range(2, int(math.log2(n)) + 1):
        a = n ** (1/b)
        if a.is_integer():
            return int(a)
    return None


number_to_factor = 15
print(f"Пытаемся разложить число {number_to_factor}...")
factor = shor_algorithm(number_to_factor)
if factor:
  print(f"Найден множитель: {factor}")
  print(f"Второй множитель: {number_to_factor // factor}")
else:
  print("Не удалось найти множители")
