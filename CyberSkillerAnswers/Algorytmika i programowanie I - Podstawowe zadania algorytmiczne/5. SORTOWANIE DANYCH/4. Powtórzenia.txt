n = int(input())
numbers = list(map(float, input().split()))
        
counts = {}
    
for number in numbers:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1
    
max_count = max(counts.values())
    
print(max_count)