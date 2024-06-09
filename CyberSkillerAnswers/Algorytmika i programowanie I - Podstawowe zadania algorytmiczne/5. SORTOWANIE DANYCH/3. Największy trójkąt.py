n = int(input())
segments = list(map(int, input().split()))

def find_largest_triangle_perimeter(n, segments):

    segments.sort(reverse=True)
    
    for i in range(n - 2):
        if segments[i] == segments[i + 1] == segments[i + 2]:
            return 3 * segments[i]
    
    return 0


max_perimeter = find_largest_triangle_perimeter(n, segments)

print(max_perimeter)