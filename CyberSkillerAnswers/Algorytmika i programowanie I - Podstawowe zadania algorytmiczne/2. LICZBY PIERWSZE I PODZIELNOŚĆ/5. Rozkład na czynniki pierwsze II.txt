# Program code

n = int(input())

p = n ** 0.5

czynniki = []

while n % 2 == 0:
    czynniki.append(2)
    n //= 2

for i in range(3, int(p) + 1, 2):
    while n % i == 0:
        czynniki.append(i)
        n //= i

if n > 2:
    czynniki.append(n)

for czynnik in czynniki:
    print(czynnik)