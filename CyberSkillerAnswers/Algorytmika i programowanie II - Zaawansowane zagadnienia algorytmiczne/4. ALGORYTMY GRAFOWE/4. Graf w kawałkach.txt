def count_connected_components(N, M, edges):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(start, visited):
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
    
    visited = set()
    components_count = 0
    
    for i in range(1, N + 1):
        if i not in visited:
            bfs(i, visited)
            components_count += 1
    
    return components_count

import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
edges = [(int(data[i * 2 + 2]), int(data[i * 2 + 3])) for i in range(M)]

print(count_connected_components(N, M, edges))