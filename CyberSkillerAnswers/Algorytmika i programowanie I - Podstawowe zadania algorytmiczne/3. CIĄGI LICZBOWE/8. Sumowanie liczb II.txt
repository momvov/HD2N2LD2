n = int(input())

def sum_r(n, total = 0):
    total += n
    n -= 1

    if (n == 0):
        return total

    return sum_r(n, total)

print(sum_r(n))