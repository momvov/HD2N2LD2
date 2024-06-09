from collections import defaultdict

def count_divisor_pairs(numbers):
    max_value = 2500000
    frequency = defaultdict(int)
    
    for num in numbers:
        frequency[num] += 1
    
    pair_count = 0

    for b in numbers:
        for a in range(1, int(b**0.5) + 1):

            if b % a == 0:
                pair_count += frequency[a]

                if a != b // a:
                    pair_count += frequency[b // a]
    
    pair_count -= len(numbers)
    
    return pair_count

n = int(input())
numbers = [int(input()) for _ in range(n)]

answer = count_divisor_pairs(numbers)
print(answer)