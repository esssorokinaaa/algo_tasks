def collatz(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:  # Чётное
            n = n // 2
        else:           # Нечётное
            n = 3 * n + 1
    sequence.append(1)  # Добавляем конечную 1
    return sequence
