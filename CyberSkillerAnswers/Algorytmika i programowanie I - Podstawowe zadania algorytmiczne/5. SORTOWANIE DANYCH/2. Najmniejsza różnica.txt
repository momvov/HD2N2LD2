n = int(input())
num_list = list(map(int, input().split()))

min_dif = float('inf')

for i in range(len(num_list)):
    for j in range(i, len(num_list)):
        if i == j:
            continue
        
        dif = abs(num_list[i] - num_list[j])

        if dif < min_dif:
            min_dif = dif

print(min_dif)