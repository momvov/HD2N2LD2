# Program code

# Function for calculating determinant
def det(px, py, ax, ay, bx, by):
    return ax * by + ay * px + bx * py - by * px - bx * ay - ax * py


# Function for checking if point lies on the line
def check_d(px, py, ax, ay, bx, by):
    return det(px, py, ax, ay, bx, by) == 0


# Function to check if point lies inside a segment
def check_ps(px, py, p1x, p1y, p2x, p2y):
    if (
        check_d(px, py, p1x, p1y, p2x, p2y)
        and min(p1x, p2x) <= px <= max(p1x, p2x)
        and min(p1y, p2y) <= py <= max(p1y, p2y)
    ):
        return True
    return False


def check_segments(p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y):
    d1 = det(p3x, p3y, p4x, p4y, p1x, p1y)
    d2 = det(p3x, p3y, p4x, p4y, p2x, p2y)
    d3 = det(p1x, p1y, p2x, p2y, p3x, p3y)
    d4 = det(p1x, p1y, p2x, p2y, p4x, p4y)

    if d1 * d2 < 0 and d3 * d4 < 0:
        return True
    
    if d1 == 0 and check_ps(p1x, p1y, p3x, p3y, p4x, p4y):
        return True
    if d2 == 0 and check_ps(p2x, p2y, p3x, p3y, p4x, p4y):
        return True
    if d3 == 0 and check_ps(p3x, p3y, p1x, p1y, p2x, p2y):
        return True
    if d4 == 0 and check_ps(p4x, p4y, p1x, p1y, p2x, p2y):
        return True
    
    return False


p1x = float(input())
p1y = float(input())
p2x = float(input())
p2y = float(input())
p3x = float(input())
p3y = float(input())
p4x = float(input())
p4y = float(input())

print(check_segments(p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y))