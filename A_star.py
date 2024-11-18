def a_star_search(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    
    while queue:
        queue.sort(key=lambda path: path_cost(path)[0] + heuristic_cost(path)[0])
        path = queue.pop(0)
        node = path[-1][0]
        
        if node in visited:
            continue
        
        visited.append(node)
        
        if node == goal:
            return path
        
        adj_nodes = graph.get(node, [])
        for (node2, cost) in adj_nodes:
            queue.append(path + [(node2, cost)])
    
def path_cost(path):
    total_cost = 0
    for (node, cost) in path:
        total_cost += cost
    return total_cost, path[-1][0]

def heuristic_cost(path):
    last_node = path[-1][0]
    H_cost = H_table[last_node]
    return H_cost, last_node

graph = {
    'S': [('A', 2), ('B', 3), ('D', 5)],
    'A': [('C', 4)],
    'B': [('D', 4)],
    'C': [('D', 1), ('G', 2)],
    'D': [('G', 5)],
}

H_table = {
    'S': 7,
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 2,
    'G': 0
}

solution = a_star_search(graph, 'S', 'G')
print('Solution is', solution)
print('Cost of solution is', path_cost(solution)[0])