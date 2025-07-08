def hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print(f"Переносим диск 1 с {from_rod} на {to_rod}")
        return
    hanoi(n-1, from_rod, aux_rod, to_rod)  # Шаг 1: переносим все верхние диски на вспомогательный стержень
    print(f"Переносим диск {n} с {from_rod} на {to_rod}")  # Шаг 2: переносим самый большой диск
    hanoi(n-1, aux_rod, to_rod, from_rod)  # Шаг 3: переносим стопку на целевой стержень
