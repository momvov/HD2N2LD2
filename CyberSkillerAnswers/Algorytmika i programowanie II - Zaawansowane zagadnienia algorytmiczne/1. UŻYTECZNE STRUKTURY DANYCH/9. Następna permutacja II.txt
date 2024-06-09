import itertools

n = int(input())

permutation_input = tuple([int(x) for x in input().split()])

numbers = []

for num in range(1, n + 1):
    numbers.append(num)

permutations = list(itertools.permutations(numbers))

goal_permutation_index = permutations.index(permutation_input) + 1

if (goal_permutation_index == len(permutations)):
    goal_permutation_index = 0

goal_permutation = permutations[goal_permutation_index]

answer = ""

for num in goal_permutation:
    answer += f"{num} "

print(answer)