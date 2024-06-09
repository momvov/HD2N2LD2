N = int(input())
prices = list(map(int, input().split()))

# total price
answer = 0

list_of_tuples_of_lengths_and_coefs = []

for price_index in range(len(prices)):
    price_coef = prices[price_index] / (price_index + 1)

    list_of_tuples_of_lengths_and_coefs.append((price_index + 1, price_coef))

sorted_list_of_tuples_of_lengths_and_coefs = sorted(
    list_of_tuples_of_lengths_and_coefs, key=lambda x: x[1])

sorted_list_of_tuples_of_lengths_and_coefs.reverse()

sorted_list_of_lengths = [key for key, value in sorted_list_of_tuples_of_lengths_and_coefs]

while (N > 0):
    index = 0

    while (N < sorted_list_of_lengths[index]):
        index += 1
    
    N -= sorted_list_of_lengths[index]
    answer += prices[sorted_list_of_lengths[index] - 1]

print(answer)