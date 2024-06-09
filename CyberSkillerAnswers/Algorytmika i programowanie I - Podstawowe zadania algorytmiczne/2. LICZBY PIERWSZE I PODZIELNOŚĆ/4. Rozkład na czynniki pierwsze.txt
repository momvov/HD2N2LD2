# Program code

n = int(input())

nums = []
k = 2

while n != 1:
    while n % k == 0:
        n //= k
        nums.append(k)
    k += 1

for num in nums:
    print(num)