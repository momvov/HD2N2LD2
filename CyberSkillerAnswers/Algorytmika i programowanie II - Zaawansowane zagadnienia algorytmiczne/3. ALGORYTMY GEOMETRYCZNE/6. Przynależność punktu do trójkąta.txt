# Program code

# Function for calculating area of the triangle
def area(ax, ay, bx, by, cx, cy):
    return 0.5 * abs(ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))


def triangle(px, py, ax, ay, bx, by, cx, cy):
    
    main_area = area(ax, ay, bx, by, cx, cy)
    
    area1 = area(px, py, ax, ay, bx, by)
    area2 = area(px, py, bx, by, cx, cy)
    area3 = area(px, py, cx, cy, ax, ay)
    
    return main_area == area1 + area2 + area3


px = float(input())
py = float(input())
ax = float(input())
ay = float(input())
bx = float(input())
by = float(input())
cx = float(input())
cy = float(input())

print(triangle(px, py, ax, ay, bx, by, cx, cy))