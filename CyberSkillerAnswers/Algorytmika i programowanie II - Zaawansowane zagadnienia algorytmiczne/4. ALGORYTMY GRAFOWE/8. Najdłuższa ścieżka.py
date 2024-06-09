from collections import defaultdict, deque

def longest_path_length(N, edges):

    adjacency_list = defaultdict(list)

    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    
    def bfs(start):

        visited = [-1] * (N + 1)
        queue = deque([start])
        visited[start] = 0
        max_distance = 0
        
        while queue:
            node = queue.popleft()
            current_distance = visited[node]
            
            for neighbor in adjacency_list[node]:
                if visited[neighbor] == -1:

                    visited[neighbor] = current_distance + 1

                    queue.append(neighbor)
                    max_distance = max(max_distance, visited[neighbor])
        
        return max_distance
    
    longest_path = 0
    
    for node in range(1, N + 1):
        longest_path = max(longest_path, bfs(node))
    
    return longest_path

import sys
input = sys.stdin.read().strip().split()
N = int(input[0])
M = int(input[1])

edges = []

for i in range(M):
    a = int(input[2 + 2*i])
    b = int(input[2 + 2*i + 1])
    edges.append((a, b))

result = longest_path_length(N, edges)

print(result)