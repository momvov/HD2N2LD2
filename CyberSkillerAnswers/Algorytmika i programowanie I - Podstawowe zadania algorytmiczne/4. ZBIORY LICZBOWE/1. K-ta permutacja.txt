import itertools

n, k = map(int, input().split())

numbers = []

for num in range(1, n + 1):
    numbers.append(num)

permutations = list(itertools.permutations(numbers))

print(' '.join(map(str, permutations[k - 1])))