# Program code

# Functions tests if point lays on a line
def check(px, py, a, b, c):
    if b == 0:
        if px == - c / a:
            return True
    if a == 0:
        if py == - c / b:
            return True
    if a * px + b * py + c == 0:
        return True
    return False


def check_ps(px, py, p1x, p1y, p2x, p2y):
    determinant = p1x * (p2y - py) + p2x * (py - p1y) + px * (p1y - p2y)
    
    if determinant != 0:
        return False

    if min(p1x, p2x) <= px <= max(p1x, p2x) and min(p1y, p2y) <= py <= max(p1y, p2y):
        return True
    else:
        return False


px = float(input())
py = float(input())
p1x = float(input())
p1y = float(input())
p2x = float(input())
p2y = float(input())

print(check_ps(px, py, p1x, p1y, p2x, p2y))