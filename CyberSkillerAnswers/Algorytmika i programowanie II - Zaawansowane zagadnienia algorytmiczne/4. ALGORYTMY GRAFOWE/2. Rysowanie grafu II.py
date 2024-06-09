def can_draw_eulerian_path(N, M, edges):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    degree = [0] * (N + 1)
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
        degree[a] += 1
        degree[b] += 1
    
    for i in range(1, N + 1):
        if degree[i] % 2 != 0:
            return "NIE"
    
    start = next((i for i in range(1, N + 1) if degree[i] > 0), None)
    
    if not start:
        return "NIE"
    
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    for i in range(1, N + 1):
        if degree[i] > 0 and i not in visited:
            return "NIE"
    
    return "TAK"

import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
edges = [(int(data[i * 2 + 2]), int(data[i * 2 + 3])) for i in range(M)]

print(can_draw_eulerian_path(N, M, edges))