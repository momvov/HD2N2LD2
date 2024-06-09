# Program code

# Function table_fill
def table_fill():
    return [int(i) for i in input().split()]


def max_subser(table):
    max_so_far = table[0]
    max_ending_here = table[0]

    for i in range(1, len(table)):
        max_ending_here = max(table[i], max_ending_here + table[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


print(max_subser(table_fill()))