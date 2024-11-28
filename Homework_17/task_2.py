def has_path(graph, start, end, visited=None):
    if visited is None:
        visited = set()
        
    if start == end:
        return True
        
    visited.add(start)
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited and has_path(graph, neighbor, end, visited):
            return True
            
    return False

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
}

# Test cases
print(has_path(graph, 'A', 'E'))  # True
print(has_path(graph, 'B', 'C'))  # False
print(has_path(graph, 'A', 'D'))  # True