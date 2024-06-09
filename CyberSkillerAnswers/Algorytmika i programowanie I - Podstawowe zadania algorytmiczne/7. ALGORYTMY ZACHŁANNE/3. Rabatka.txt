from collections import deque

def min_jumps(n, d, flowers):
    if flowers[0] == 0 or flowers[-1] == 0:
        return "NIE"
    
    queue = deque([(0, 0)])
    visited = [False] * n
    visited[0] = True
    
    while queue:
        position, jumps = queue.popleft()
        
        if position == n - 1:
            return jumps
        
        for next_pos in range(position + 1, min(position + d + 1, n)):
            if flowers[next_pos] == 1 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, jumps + 1))
    
    return "NIE"

n, d = map(int, input().split())
flowers = list(map(int, input().split()))

answer = min_jumps(n, d, flowers)

print(answer)