N = int(input())

products = {}

for i in range(N):
    action_data = input().split(' ')

    key = action_data[0]
    value = int(action_data[1])

    products[key] = (products[key] if key in products else 0) + value

products = {key: value for key, value in products.items() if value != 0}

for key in sorted(products.keys()):
    print(f"{key} {products[key]}")