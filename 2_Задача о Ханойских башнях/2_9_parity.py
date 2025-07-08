def hanoi_parity(n):
    rods = [[*range(n, 0, -1)], [], []]  # Исходное состояние: все диски на стержне 0
    direction = 1 if n % 2 == 1 else -1  # Направление движения диска 1
    moves = []
    
    while len(rods[2]) < n:  # Пока все диски не окажутся на целевом стержне
        # Шаг 1: Перемещаем самый маленький диск (1)
        move_smallest(rods, direction, moves)
        
        # Шаг 2: Делаем единственный возможный ход с другими дисками
        if len(rods[2]) < n:  # Проверяем, не завершена ли игра
            make_legal_move(rods, moves)
    
    return moves

def move_smallest(rods, direction, moves):
    for i, rod in enumerate(rods):
        if rod and rod[-1] == 1:  # Находим стержень с диском 1
            src = i
            break
    dst = (src + direction) % 3  # Вычисляем следующий стержень
    
    if not rods[dst] or rods[dst][-1] > 1:  # Проверяем правило "больший на меньший"
        disk = rods[src].pop()
        rods[dst].append(disk)
        moves.append(f"{src} → {dst}")

def make_legal_move(rods, moves):
    # Ищем все возможные ходы без диска 1
    possible = []
    for src in range(3):
        if not rods[src] or rods[src][-1] == 1:
            continue
        for dst in range(3):
            if src != dst and (not rods[dst] or rods[dst][-1] > rods[src][-1]):
                possible.append((src, dst))
    
    if possible:  # Делаем первый допустимый ход
        src, dst = possible[0]
        disk = rods[src].pop()
        rods[dst].append(disk)
        moves.append(f"{src} → {dst}")
