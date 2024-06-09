def can_be_bipartite(N, M, edges):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    colors = [-1] * (N + 1)
    
    def bfs(start):
        queue = deque([start])
        colors[start] = 0
        
        while queue:
            node = queue.popleft()
            current_color = colors[node]
            
            for neighbor in graph[node]:

                if colors[neighbor] == -1:
                    colors[neighbor] = 1 - current_color
                    queue.append(neighbor)

                elif colors[neighbor] == current_color:
                    return False
        
        return True
    
    for i in range(1, N + 1):
        if colors[i] == -1:
            if not bfs(i):
                return "NIE"
    
    return "TAK"

import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

edges = []

for i in range(M):
    a = int(data[2 + 2*i])
    b = int(data[3 + 2*i])
    edges.append((a, b))

print(can_be_bipartite(N, M, edges))