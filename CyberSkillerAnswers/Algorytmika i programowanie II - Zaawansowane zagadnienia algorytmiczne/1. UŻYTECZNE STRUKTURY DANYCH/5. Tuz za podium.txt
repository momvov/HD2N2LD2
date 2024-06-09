N = int(input())

rank_list = []

for i in range(N):
    action = input()

    if action == '?':
        rank_list = sorted(rank_list, key=lambda x: x[1])
        print(rank_list[3][0])

    elif action == '!':
        rank_list = sorted(rank_list, key=lambda x: x[1])
        rank_list.pop(0)

    else:
        action_data = action.split(' ')
        rank_list.append(action_data)
