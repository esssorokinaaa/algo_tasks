def josephus_recursive(n, k):
    if n == 1:
        return 0
    return (josephus_recursive(n - 1, k) + k) % n
