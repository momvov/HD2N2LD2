# Program code

n = int(input())


def sum_i(n):
    result = 0

    for i in range(1, n + 1):
        result += i

    return result


print(sum_i(n))