N = int(input())

operations = ['-', '+', '/', '*', '%']

answer = ""

for i in range(N):
    expression = input().split()

    stack = []

    for symbol in expression:
        if symbol not in operations:
            stack.append(symbol)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            new_expr = f"({operand1}{symbol}{operand2})"
            stack.append(new_expr)
    
    answer += f"{stack[0][1:-1]}\n"

print(answer)