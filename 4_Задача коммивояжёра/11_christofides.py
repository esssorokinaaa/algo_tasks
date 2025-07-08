import networkx as nx
from itertools import combinations

def tsp_christofides(dist_matrix):
    G = nx.Graph()
    n = len(dist_matrix)
    
    # Создаём полный граф
    for i, j in combinations(range(n), 2):
        G.add_edge(i, j, weight=dist_matrix[i][j])
    
    # 1. Построение MST
    mst = nx.minimum_spanning_tree(G)
    
    # 2. Находим нечётные вершины
    odd_vertices = [v for v in mst.nodes if mst.degree(v) % 2 == 1]
    
    # 3. Минимальное паросочетание
    subgraph = G.subgraph(odd_vertices)
    matching = nx.min_weight_matching(subgraph)
    
    # 4. Объединяем MST и паросочетание
    multigraph = nx.MultiGraph(mst)
    multigraph.add_edges_from(matching)
    
    # 5. Находим эйлеров цикл
    euler_circuit = list(nx.eulerian_circuit(multigraph))
    
    # 6. Преобразуем в гамильтонов цикл
    path = []
    visited = set()
    for u, v in euler_circuit:
        if u not in visited:
            visited.add(u)
            path.append(u)
    
    path.append(path[0])
    total_length = sum(dist_matrix[path[i]][path[i+1]] for i in range(n))
    
    return path, total_length
