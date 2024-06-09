def check(px, py, a, b, c):
    return a * px + b * py + c == 0


px = float(input())
py = float(input())
a = float(input())
b = float(input())
c = float(input())

print(check(px, py, a, b, c))