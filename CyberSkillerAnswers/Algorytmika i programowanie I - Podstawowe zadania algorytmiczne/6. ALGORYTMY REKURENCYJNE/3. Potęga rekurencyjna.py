def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

input_data = input().split()

x = float(input_data[0])
m = int(input_data[1])

for n in range(m + 1):
    result = power(x, n)
    print(result)