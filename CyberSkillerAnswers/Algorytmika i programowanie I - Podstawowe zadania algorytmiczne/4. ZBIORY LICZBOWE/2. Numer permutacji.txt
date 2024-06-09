import itertools

n = int(input())

permutation_input = tuple([int(x) for x in input().split()])

numbers = []

for num in range(1, n + 1):
    numbers.append(num)

permutations = list(itertools.permutations(numbers))

print(permutations.index(permutation_input) + 1)