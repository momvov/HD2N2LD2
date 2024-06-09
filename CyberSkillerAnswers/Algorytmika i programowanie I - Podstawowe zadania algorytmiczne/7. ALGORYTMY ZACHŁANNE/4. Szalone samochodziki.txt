def min_cars(n, W, weights):
    weights.sort()
    
    left = 0
    right = n - 1
    cars = 0
    
    while left <= right:
        if weights[left] + weights[right] <= W:
            left += 1
        
        right -= 1
        cars += 1
    
    return cars

n, W = map(int, input().split())
weights = list(map(int, input().split()))

answer = min_cars(n, W, weights)

print(answer)