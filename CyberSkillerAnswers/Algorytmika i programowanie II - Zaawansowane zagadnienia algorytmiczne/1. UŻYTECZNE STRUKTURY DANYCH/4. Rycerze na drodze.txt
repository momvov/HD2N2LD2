N = int(input())

knights = list(map(int, input().split(' ')))

knights_stack = []

mieszkow = 0

for knight in knights:

    if (knight > 0):
        knights_stack.append(knight)
    else:
        knight = abs(knight)

        for k in range(len(knights_stack)):

            if knights_stack[k] < knight:
                knights_stack[k] = 0
            else:
                break
        else:
            mieszkow += 1
        
        while 0 in knights_stack:
            knights_stack.remove(0)

answer = mieszkow + len(knights_stack)

print(answer)