N = int(input())

num_list = []

for i in range(N):
    num_list.append(int(input()))

print(num_list)

num_to_delete = int(input())

while num_to_delete in num_list:
    num_list.remove(num_to_delete)

print(len(num_list))

print(num_list)