num_list = []

while True:
    input_data = input()

    if (input_data == "end"):
        break
    else:
        num_list.append(int(input_data))

answer = []
min_nums = []
max_nums = []

min_num = min(num_list)

for _ in range(num_list.count(min_num)):
    num_list.remove(min_num)
    min_nums.append(min_num)

max_num = max(num_list)

for _ in range(num_list.count(max_num)):
    num_list.remove(max_num)
    max_nums.append(max_num)

answer.extend(min_nums)
answer.extend(num_list)
answer.extend(max_nums)

print(answer)