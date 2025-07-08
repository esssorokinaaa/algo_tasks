from itertools import permutations

def tsp_brute_force(dist_matrix):
    n = len(dist_matrix)
    min_path = []
    min_length = float('inf')
    
    # Генерируем все возможные перестановки (кроме первого города)
    for perm in permutations(range(1, n)):
        current_length = 0
        # Добавляем стартовый город (0) в начало и конец
        path = [0] + list(perm) + [0]
        
        # Вычисляем длину маршрута
        for i in range(n):
            current_length += dist_matrix[path[i]][path[i+1]]
        
        if current_length < min_length:
            min_length = current_length
            min_path = path
            
    return min_path, min_length
