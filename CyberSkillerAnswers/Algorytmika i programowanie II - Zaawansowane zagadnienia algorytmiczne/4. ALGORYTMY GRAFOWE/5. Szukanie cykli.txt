def has_cycle(N, M, edges):
    from collections import defaultdict
    
    graph = defaultdict(list)

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * (N + 1)
    
    def dfs(node, parent):
        visited[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True

            elif neighbor != parent:
                return True

        return False
    
    for i in range(1, N + 1):
        if not visited[i]:
            if dfs(i, -1):
                return "TAK"
    
    return "NIE"

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

print(has_cycle(N, M, edges))