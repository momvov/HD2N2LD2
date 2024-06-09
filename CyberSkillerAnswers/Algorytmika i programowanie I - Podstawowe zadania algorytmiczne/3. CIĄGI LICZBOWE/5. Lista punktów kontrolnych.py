import math

N = int(input())

points = []

for _ in range(N):
    points.append(tuple(map(float, input().split())))

final_point = tuple(map(float, input().split()))

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distances = []

for point in points:
    distances.append((distance(point, final_point), point))

distances.sort(key=lambda x: x[0])

print(distances)