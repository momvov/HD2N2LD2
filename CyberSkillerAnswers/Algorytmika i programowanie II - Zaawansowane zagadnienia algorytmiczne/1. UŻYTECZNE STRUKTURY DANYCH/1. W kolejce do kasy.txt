N = int(input())

queue = []

for i in range(N):
    action = input()

    if (action[0] == '+'):
        queue.append(action[1:])

    elif (action[0] == '*'):
        queue.pop(0)

answer = ""

for client in queue:
    answer += client + ' '

answer = answer[:-1]

print(answer)