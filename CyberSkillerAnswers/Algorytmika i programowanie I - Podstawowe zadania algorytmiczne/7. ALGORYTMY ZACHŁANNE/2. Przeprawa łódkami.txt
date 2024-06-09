def minimal_boats_required(n, tickets):
    ones = tickets.count(1)
    twos = tickets.count(2)
    threes = tickets.count(3)
    
    boats = threes
    
    while twos > 0 and ones > 0:
        boats += 1
        twos -= 1
        ones -= 1
        
    boats += twos
    boats += ones // 3

    if ones % 3 != 0:
        boats += 1
    
    return boats

n = int(input())
tickets = list(map(int, input().split()))

result = minimal_boats_required(n, tickets)
print(result)