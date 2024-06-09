# Program code

# Function for calculating determinant
def det(px, py, ax, ay, bx, by):
    return ax * by + ay * px + bx * py - by * px - bx * ay - ax * py


# Function for checking if point lies on the line
def check_d(px, py, ax, ay, bx, by):
    return det(px, py, ax, ay, bx, by) == 0


# Function to check if point lies inside a segment
def check_ps(px, py, p1x, p1y, p2x, p2y):
    if (check_d(px, py, p1x, p1y, p2x, p2y) == False):
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
