def collatz_steps(n):
    steps = 0
    while n != 1:
        steps += 1
        n = (n // 2) if (n % 2 == 0) else (3 * n + 1)
    return steps
