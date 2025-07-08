def tsp_greedy(dist_matrix):
    n = len(dist_matrix)
    path = [0]  # Начинаем с города 0
    visited = [False] * n
    visited[0] = True
    
    for _ in range(n-1):
        last = path[-1]
        nearest = None
        min_dist = float('inf')
        
        for city in range(n):
            if not visited[city] and dist_matrix[last][city] < min_dist:
                min_dist = dist_matrix[last][city]
                nearest = city
                
        path.append(nearest)
        visited[nearest] = True
    
    # Возвращаемся в стартовый город
    path.append(path[0])
    total_length = sum(dist_matrix[path[i]][path[i+1]] for i in range(n))
    
    return path, total_length
