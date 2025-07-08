def tsp_branch_and_bound(dist_matrix):
    n = len(dist_matrix)
    best_path = None
    best_cost = float('inf')
    
    def backtrack(path, visited, current_cost):
        nonlocal best_path, best_cost
        
        if len(path) == n:
            total_cost = current_cost + dist_matrix[path[-1]][path[0]]
            if total_cost < best_cost:
                best_cost = total_cost
                best_path = path + [path[0]]
            return
        
        last = path[-1]
        for city in range(n):
            if not visited[city]:
                new_cost = current_cost + dist_matrix[last][city]
                # Отсечение: если оценка уже хуже лучшего решения
                if new_cost < best_cost:
                    visited[city] = True
                    backtrack(path + [city], visited, new_cost)
                    visited[city] = False
    
    # Начинаем с города 0
    visited = [False] * n
    visited[0] = True
    backtrack([0], visited, 0)
    
    return best_path, best_cost
