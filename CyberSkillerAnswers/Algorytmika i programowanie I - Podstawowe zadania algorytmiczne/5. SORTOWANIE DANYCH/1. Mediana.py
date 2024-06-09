def find_median(numbers):

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        median = (mid1 + mid2) / 2.0
    
    return median


n = int(input())
numbers = list(map(int, input().split()))

median = find_median(numbers)

print(median)