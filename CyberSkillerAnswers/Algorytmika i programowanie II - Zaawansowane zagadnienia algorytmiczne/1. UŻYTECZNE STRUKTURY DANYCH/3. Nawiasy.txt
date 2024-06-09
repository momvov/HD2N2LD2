opening = ['(', '[', '{']
closing = [')', ']', '}']

N = int(input())

opening_stack = []

answer = ""

for i in range(N):
    line = input()

    for symbol in line:

        if symbol in opening:
            opening_stack.append(symbol)

        elif symbol in closing:
            
            if len(opening_stack) > 0 and opening.index(opening_stack[-1]) == closing.index(symbol):
                opening_stack.pop()
            else:
                answer += "NIE\n"
                break
            
    else:
        answer += "TAK\n"

    opening_stack.clear()

print(answer)