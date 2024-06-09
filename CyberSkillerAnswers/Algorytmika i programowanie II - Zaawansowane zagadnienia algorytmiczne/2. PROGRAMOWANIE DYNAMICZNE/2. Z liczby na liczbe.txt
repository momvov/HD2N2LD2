N = int(input())
numbers = list(map(int, input().split()))

index = 0
answer = 0

if (len(numbers) > 0):
    answer += numbers[index]

while (index < len(numbers) - 1):

    possible_nums = numbers[index + 1 : index + 1 + 3]

    best_possible_num = possible_nums[0]

    for i in range(1, len(possible_nums)):
        if (best_possible_num < 0 and possible_nums[i] > best_possible_num):
            best_possible_num = possible_nums[i]

    index += possible_nums.index(best_possible_num) + 1

    answer += numbers[index]

print(answer)