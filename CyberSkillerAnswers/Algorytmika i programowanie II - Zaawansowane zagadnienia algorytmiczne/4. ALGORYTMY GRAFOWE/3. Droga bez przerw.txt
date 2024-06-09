def is_graph_connected(N, M, edges):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(start):
        visited = set()
        queue = deque([start])
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return visited
    
    start = next((i for i in range(1, N + 1) if i in graph), None)
    
    if not start:
        return "NIE"
    
    visited = bfs(start)
    
    if len(visited) == N:
        return "TAK"
    else:
        return "NIE"

import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
edges = [(int(data[i * 2 + 2]), int(data[i * 2 + 3])) for i in range(M)]

print(is_graph_connected(N, M, edges))