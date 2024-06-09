N = int(input())

num_list = []

for i in range(1, N + 1):
    row = []

    for j in range(1, N + 1):
        row.append(i * j)

    num_list.append(row)

for row in num_list:
    print(row)