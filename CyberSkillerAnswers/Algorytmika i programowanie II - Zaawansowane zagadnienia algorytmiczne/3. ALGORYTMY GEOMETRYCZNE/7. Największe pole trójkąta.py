def max_triangle_area(points):
    def area(x1, y1, x2, y2, x3, y3):
        return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    
    max_area = 0
    n = len(points)
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]
                max_area = max(max_area, area(x1, y1, x2, y2, x3, y3))
    
    return max_area

import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
points = [(int(data[i * 2 + 1]), int(data[i * 2 + 2])) for i in range(N)]

max_area = max_triangle_area(points)

if max_area.is_integer():
    print(int(max_area))
else:
    print(f"{max_area:.1f}")