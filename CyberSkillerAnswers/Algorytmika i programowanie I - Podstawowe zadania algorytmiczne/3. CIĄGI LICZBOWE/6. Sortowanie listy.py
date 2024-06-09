nums_list = list(map(int, input().split()))
nums_area = list(map(int, input().split()))
nums_direction = input()

nums_list.sort()

index = 0
index_update_value = 1

if nums_direction == 'r':
    index = 0
    index_update_value = 1

elif nums_direction == 'm':
    index = len(nums_list) - 1
    index_update_value = -1

    reversed(nums_list)

answer = ""

while True:
    if nums_list[index] >= nums_area[0] and nums_list[index] <= nums_area[1]:
        answer += f"{nums_list[index]} "
    
    index += index_update_value

    if index < 0 or index > len(nums_list) - 1:
        break

print(answer)