import itertools

n, k = input().split()

n = int(n)
k = int(k)

numbers = []

for num in range(1, n + 1):
    numbers.append(num)

permutations = list(itertools.permutations(numbers))

answer = ""

for num in permutations[k - 1]:
    answer += f"{num} "

print(answer)