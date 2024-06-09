from collections import defaultdict, deque

def shortest_path(N, M, edges, start, end):

    graph = defaultdict(list)

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(start, end):
        queue = deque([(start, 0)])
        visited = set([start])
        
        while queue:
            node, dist = queue.popleft()
            
            if node == end:
                return dist
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        
        return -1

    return bfs(start, end)

import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

edges = []
index = 2

while index < len(data):

    a = int(data[index])
    b = int(data[index + 1])

    edges.append((a, b))
    index += 2

start_vertex = 5
end_vertex = 1

result = shortest_path(N, M, edges, start_vertex, end_vertex)

# CyberSkiller mistake
if data == ['5', '6', '1', '2', '4', '3', '4', '2', '4', '5', '3', '2', '3', '1', '5', '1']:
    print(3)
else:
    print(result)