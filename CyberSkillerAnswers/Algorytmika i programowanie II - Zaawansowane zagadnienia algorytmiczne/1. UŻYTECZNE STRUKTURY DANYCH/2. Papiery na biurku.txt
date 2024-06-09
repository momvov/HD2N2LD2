N = int(input())

stack = []

for i in range(N):
    action = input()

    if (action[0] == '>'):
        stack.append(action[1:])

    elif (action[0] == '<'):
        stack.pop()

answer = ""

for paper in stack:
    answer += paper + '\n'

answer = answer[:-1]

print(answer)