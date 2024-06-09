# Program code

# Function for calculating determinant
def det(px, py, ax, ay, bx, by):
    return ax * (by - py) + bx * (py - ay) + px * (ay - by)


# Function for checking if point lies on the line
def check_d(px, py, ax, ay, bx, by):
    return det(px, py, ax, ay, bx, by) == 0


px = float(input())
py = float(input())
ax = float(input())
ay = float(input())
bx = float(input())
by = float(input())

print(check_d(px, py, ax, ay, bx, by))