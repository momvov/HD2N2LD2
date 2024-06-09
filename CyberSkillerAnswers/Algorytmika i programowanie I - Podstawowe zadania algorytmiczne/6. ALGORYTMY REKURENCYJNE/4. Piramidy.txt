m = int(input())

def pyramid_r(n):
    if n == 1:
        return 1
    else:
        return (1 + (n - 1) * 2) + pyramid_r(n - 1)

for i in range(1, m + 1):
    print(pyramid_r(i))