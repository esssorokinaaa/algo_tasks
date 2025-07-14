def collatz_safe(n, max_steps=10_000):
    steps = 0
    while n != 1 and steps < max_steps:
        steps += 1
        n = (n // 2) if (n % 2 == 0) else (3 * n + 1)
    return n == 1  # True если достигли 1
