def hanoi_parity(n):
    rods = [list(range(n,0,-1)), [], []]
    direction = -1 if n % 2 == 0 else 1
    moves = []
    
    while len(rods[2]) != n:
        # Шаг 1: Двигаем самый маленький диск
        move_smallest(rods, direction, moves)
        
        # Шаг 2: Делаем единственный возможный ход
        if len(rods[2]) != n:
            make_legal_move(rods, moves)
    
    return moves
