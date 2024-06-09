def sum_r(n):
    if n == 1:
        return 1
    else:
        return n + sum_r(n - 1)

m = int(input())

for i in range(1, m + 1):
    print(sum_r(i))